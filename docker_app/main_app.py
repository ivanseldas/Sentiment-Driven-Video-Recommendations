from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import logging
import os
import joblib
import random
import pandas as pd

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

final_matrix = None
emotion_df = None
load_errors = {}

def load_artifacts():
    global final_matrix, emotion_df, load_errors
    try:
        logger.info("Loading final_score_matrix.joblib ...")
        final_matrix = joblib.load('final_score_matrix.joblib')
        logger.info(f"Loaded similarity matrix with shape {final_matrix.shape}")
    except Exception as e:
        load_errors['final_matrix'] = str(e)
        logger.exception("Error loading final_score_matrix.joblib")
    try:
        logger.info("Loading df_avg_emotions.csv ...")
        emotion_df = pd.read_csv('df_avg_emotions.csv', index_col=0).set_index('video_id')
        if 'final_emotion_score' in emotion_df.columns:
            emotion_df.drop(columns='final_emotion_score', inplace=True)
        logger.info(f"Loaded emotions df with shape {emotion_df.shape}")
    except Exception as e:
        load_errors['emotion_df'] = str(e)
        logger.exception("Error loading df_avg_emotions.csv")

load_artifacts()

# Route to serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API route to get recommendations
@app.get("/api/recommendations/", response_class=JSONResponse)
async def get_recommendations(video_id: str = None):
    if final_matrix is None:
        return JSONResponse(content={"error": "Similarity matrix not loaded"}, status_code=500)
    # Pick a valid initial video if none provided or id not present
    if video_id is None or video_id not in final_matrix.columns:
        initial_video = random.choice(final_matrix.index.tolist())
    else:
        initial_video = video_id

    # Defensive: avoid KeyError if column missing
    if initial_video not in final_matrix.columns:
        return JSONResponse(content={"error": "Initial video not in matrix"}, status_code=404)

    top_10_videos = final_matrix[initial_video].sort_values(ascending=False).head(10)
    recommendations = {
        "initial_video": initial_video,
        "top_10_videos": [
            {"id": vid, "score": float(score)} for vid, score in top_10_videos.items()
        ]
    }
    return JSONResponse(content=recommendations)

# API route to get emotion scores for a specific video
@app.get("/api/emotion_scores/{video_id}", response_class=JSONResponse)
async def get_emotion_scores(video_id: str):
    if emotion_df is None or video_id not in emotion_df.index:
        return JSONResponse(content={"error": "Video ID not found"}, status_code=404)
    
    emotion_scores = emotion_df.loc[video_id].to_dict()
    return JSONResponse(content=emotion_scores)

# Simple health/ready endpoint
@app.get("/health", response_class=JSONResponse)
async def health():
    status = 'ok' if load_errors == {} and final_matrix is not None and emotion_df is not None else 'degraded'
    payload = {
        'status': status,
        'final_matrix_loaded': final_matrix is not None,
        'emotion_df_loaded': emotion_df is not None,
        'errors': load_errors,
        'cwd': os.getcwd()
    }
    code = 200 if status == 'ok' else 500 if load_errors else 206
    return JSONResponse(content=payload, status_code=code)
