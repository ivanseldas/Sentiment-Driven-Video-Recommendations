from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import joblib
import random
import pandas as pd

app = FastAPI()

# Load the final_score_matrix from the joblib file (assumed to be a pandas DataFrame)
final_matrix = joblib.load('final_score_matrix.joblib')

# Sample emotion scores DataFrame (replace with real data)
emotion_df = pd.read_csv('df_avg_emotions.csv', index_col=0).set_index('video_id')
if 'final_emotion_score' in emotion_df.columns:
    emotion_df.drop(columns='final_emotion_score', inplace=True)

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
                color: #ffffff; 
                height: 100vh;
                margin: 0;
            }
            h1 {
                font-size: 24px;
                color: #ffffff;
                margin: 20px 0;
            }
            .container { 
                display: flex; 
                width: 960px; 
                max-width: 100vw;
                height: auto;
                background-color: #181818;
            }
            .video-section {
                display: flex;
                flex-direction: column;
                width: 640px;
                margin-right: 20px;
            }
            .video-player { 
                width: 100%;
                height: 360px;
                margin-bottom: 20px;
            }
            .video-player iframe { 
                width: 100%; 
                height: 100%; 
            }
            .graph-container {
                width: 100%;
                padding: 10px;
                background-color: #181818;
                border-radius: 8px;
                margin-top: 20px;
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                max-height: 400px;
                overflow-y: auto;
            }
            .graph-title {
                color: #ffffff;
                font-size: 20px;
                margin-bottom: 15px;
                text-align: center;
                width: 100%;
            }
            .emotion-bar {
                display: flex;
                align-items: center;
                margin-bottom: 8px;
                width: 100%;
            }
            .emotion-label {
                width: 80px;
                color: #fff;
                font-size: 14px;
                margin-right: 10px;
                text-transform: capitalize;
                flex-shrink: 0;
            }
            .emotion-score {
                height: 22px;
                background-color: #007bff;
                border-radius: 5px;
                color: #fff;
                font-weight: bold;
                font-size: 12px;
                line-height: 22px;
                padding-left: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%; /* Set max width of the bar to 400px */
                margin-left: 25px; /* Add margin to avoid clashing with label */
            }
            .no-comments {
                color: #ff6f61;
                font-size: 16px;
                margin-top: 10px;
                text-align: center;
                width: 100%;
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
                color: #007bff;
            }
        </style>
    </head>
    <body>
        <h1>SENTIMENT DRIVEN RECOMMENDATION</h1>
        <div class="container">
            <div class="video-section">
                <div class="video-player">
                    <iframe id="video-frame" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                </div>
                <div class="graph-container">
                    <div class="graph-title">Top 10 Emotions from Comments</div>
                    <div id="emotion-scores" class="emotion-scores">
                        <!-- Top 10 Emotion bars will be generated here -->
                    </div>
                </div>
            </div>
            <div class="recommendations">
                <h2>Recommended Videos</h2>
                <div id="video-list"></div>
            </div>
        </div>
        
        <script>
            const videoList = document.getElementById('video-list');
            const videoFrame = document.getElementById('video-frame');
            const emotionScoresDiv = document.getElementById("emotion-scores");

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
                    title.textContent = video.id;

                    const score = document.createElement('span');
                    score.className = 'score';
                    score.textContent = `Score: ${video.score.toFixed(2)}`;

                    box.appendChild(thumbnail);
                    box.appendChild(title);
                    box.appendChild(score);
                    box.onclick = () => loadVideo(video.id);
                    videoList.appendChild(box);
                });

                // Load the emotion scores for the initial or selected video
                loadEmotionScores(data.initial_video);
            }

            function loadVideo(videoId) {
                // Set the video frame to the selected video ID
                videoFrame.src = `https://www.youtube.com/embed/${videoId}`;

                // Fetch recommendations and emotion scores for the currently playing video
                fetchRecommendations(videoId);  // Update recommendations
                loadEmotionScores(videoId);     // Update emotion scores for the current video
            }

            // Fetch the emotion scores for a given video ID and display them
            async function loadEmotionScores(videoId) {
                const response = await fetch(`/api/emotion_scores/${videoId}`);
                const emotionScores = await response.json();
                
                // Clear any existing scores
                emotionScoresDiv.innerHTML = '';

                // Sort and get the top 10 emotions by score, excluding NaN or null values
                const top10Emotions = Object.entries(emotionScores)
                    .filter(([emotion, score]) => score !== null && !isNaN(score))  // Filter out null and NaN values
                    .sort((a, b) => b[1] - a[1]) // Sort by score in descending order
                    .slice(0, 10); // Take the top 10 scores

                // If there are no valid emotions, display "No Comments" message
                if (top10Emotions.length === 0) {
                    const noCommentsMessage = document.createElement('div');
                    noCommentsMessage.className = 'no-comments';
                    noCommentsMessage.textContent = "No Comments";
                    emotionScoresDiv.appendChild(noCommentsMessage);
                } else {
                    // Create and display bars for each top emotion
                    top10Emotions.forEach(([emotion, score]) => {
                        const barContainer = document.createElement('div');
                        barContainer.className = 'emotion-bar';

                        const label = document.createElement('span');
                        label.className = 'emotion-label';
                        label.textContent = `${emotion}:`;

                        const bar = document.createElement('div');
                        bar.className = 'emotion-score';
                        const maxBarWidth = 475; // Maximum width in pixels
                        const barWidth = Math.min(score * maxBarWidth, maxBarWidth); // Calculate width based on score
                        bar.style.width = `${barWidth}px`; // Set the width in pixels                        
                        bar.textContent = score.toFixed(2);  // Display the raw score from 0 to 1
                        barContainer.appendChild(label);
                        barContainer.appendChild(bar);
                        emotionScoresDiv.appendChild(barContainer);
                    });
                }
            }

            // Initial load of recommendations and emotion scores
            fetchRecommendations();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# API route to get recommendations
@app.get("/api/recommendations/", response_class=JSONResponse)
async def get_recommendations(video_id: str = None):
    if video_id is None:
        initial_video = random.choice(final_matrix.index)
    else:
        initial_video = video_id
    
    top_10_videos = final_matrix[initial_video].sort_values(ascending=False)[:10]
    
    recommendations = {
        "initial_video": initial_video,
        "top_10_videos": [
            {"id": video_id, "score": score} for video_id, score in top_10_videos.items()
        ]
    }
    
    return JSONResponse(content=recommendations)

# API route to get emotion scores for a specific video
@app.get("/api/emotion_scores/{video_id}", response_class=JSONResponse)
async def get_emotion_scores(video_id: str):
    if video_id not in emotion_df.index:
        return JSONResponse(content={"error": "Video ID not found"}, status_code=404)
    
    emotion_scores = emotion_df.loc[video_id].to_dict()
    return JSONResponse(content=emotion_scores)
