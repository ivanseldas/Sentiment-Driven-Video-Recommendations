from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import joblib
import random
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the final_score_matrix from the joblib file (assumed to be a pandas DataFrame)
final_matrix = joblib.load('final_score_matrix.joblib')

# Sample emotion scores DataFrame (replace with real data)
emotion_df = pd.read_csv('df_avg_emotions.csv', index_col=0).set_index('video_id')
if 'final_emotion_score' in emotion_df.columns:
    emotion_df.drop(columns='final_emotion_score', inplace=True)

# Route to serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
