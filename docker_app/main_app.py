from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import joblib
import random

app = FastAPI()

# Load the final_score_matrix from the joblib file (assumed to be a pandas DataFrame)
final_matrix = joblib.load('final_score_matrix.joblib')

# Route to serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def main_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sentiment Driven Recommendation</title>
        <link href="https://fonts.googleapis.com/css2?family=Oxanium:wght@300&display=swap" rel="stylesheet">
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { 
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                font-family: 'Oxanium', sans-serif; 
                background-color: #181818; 
                color: #fff; 
                height: 100vh;
                margin: 0;
            }
            h1 {
                font-size: 24px;
                color: #fff;
                margin: 20px 0;
            }
            .container { 
                display: flex; 
                width: 960px; 
                max-width: 100vw;
                height: auto;
                background-color: #181818;
            }
            .video-player { 
                width: 640px;
                height: 360px;
            }
            .video-player iframe { 
                width: 100%; 
                height: 100%; 
            }
            .recommendations { 
                width: 320px;
                padding: 10px; 
                overflow-y: auto;
            }
            .recommendations h2 { 
                color: #fff; 
                font-size: 1.2em; 
                margin-bottom: 10px;
            }
            .recommendation-box { 
                display: flex; 
                align-items: center; 
                margin-bottom: 10px; 
                cursor: pointer; 
                color: #fff; 
            }
            .thumbnail { 
                width: 80px; 
                height: auto; 
                margin-right: 10px; 
            }
            .title { 
                font-size: 14px; 
                color: #ccc; 
            }
            .title:hover { 
                color: #fff; 
            }
            .score { 
                margin-left: 10px; 
                font-size: 12px; 
                color: #ffcc00; /* Use a different color for score */
            }
        </style>
    </head>
    <body>
        <h1>SENTIMENT DRIVEN RECOMMENDATION</h1>
        <div class="container">
            <div class="video-player">
                <iframe id="video-frame" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
            <div class="recommendations">
                <h2>Recommended Videos</h2>
                <div id="video-list"></div>
            </div>
        </div>
        
        <script>
            const videoList = document.getElementById('video-list');
            const videoFrame = document.getElementById('video-frame');

            // Fetch recommendations for a given video ID
            async function fetchRecommendations(videoId = null) {
                const url = videoId ? `/api/recommendations/?video_id=${videoId}` : "/api/recommendations/";
                const response = await fetch(url);
                const data = await response.json();

                // Load the selected video (if any) or the initial random video
                videoFrame.src = `https://www.youtube.com/embed/${data.initial_video}`;
                
                // Display recommended videos with scores
                videoList.innerHTML = '';
                data.top_10_videos.forEach(video => {
                    const box = document.createElement('div');
                    box.className = 'recommendation-box';

                    const thumbnail = document.createElement('img');
                    thumbnail.src = `https://i.ytimg.com/vi/${video.id}/default.jpg`;
                    thumbnail.className = 'thumbnail';

                    const title = document.createElement('span');
                    title.className = 'title';
                    title.textContent = video.id;  // Display the video ID as title

                    const score = document.createElement('span');
                    score.className = 'score';
                    score.textContent = `Score: ${video.score.toFixed(2)}`;  // Display the final score

                    box.appendChild(thumbnail);
                    box.appendChild(title);
                    box.appendChild(score);
                    box.onclick = () => loadVideo(video.id);
                    videoList.appendChild(box);
                });
            }

            function loadVideo(videoId) {
                videoFrame.src = `https://www.youtube.com/embed/${videoId}`;
                fetchRecommendations(videoId);  // Fetch recommendations for the selected video
            }

            // Initial load of recommendations
            fetchRecommendations();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# API route to get recommendations
@app.get("/api/recommendations/", response_class=JSONResponse)
async def get_recommendations(video_id: str = None):
    # If no video ID is passed, set a random video as the initial one
    if video_id is None:
        initial_video = random.choice(final_matrix.index)
    else:
        initial_video = video_id
    
    # Recommend the top 10 videos based on the similarity score
    top_10_videos = final_matrix[initial_video].sort_values(ascending=False)[:10]
    
    # Prepare the recommendations as a list of video IDs and scores
    recommendations = {
        "initial_video": initial_video,
        "top_10_videos": [
            {"id": video_id, "score": score} for video_id, score in top_10_videos.items()
        ]
    }
    
    return JSONResponse(content=recommendations)