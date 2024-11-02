# **Sentiment-Driven Video Recommendations**

- **End-to-end Personalized Video Recommendation System** driven by Natural Language Processing (NLP) and Machine Learning (ML), with recommendations based on:
    - **Video Content**: TF-IDF analysis of video transcripts.
    - **Sentiment Analysis**: Comment sentiment score from RoBERTa (Huggingface).
    - **Clustering**: Unsupervised ML for grouping videos.
- **Methodology**:
    - Constructs a **Cosine Similarity Matrix** (TF-IDF).
    - Enhances with **Sentiment** and **Clustering Scores** for refined recommendations.

[Link to website](https://video-recommendation-project-321465604500.us-central1.run.app/)
![image](https://github.com/user-attachments/assets/0748f0fc-5b27-4dce-8abf-ca0e094932be)

---

## Final Score Calculation

The final score is calculated as follows:

$$
\text{Final Score} = \text{Cosine Similarity Matrix} \times \text{Sentiment Score} \times \text{Cluster Boost}
$$

where:

$$
\text{Sentiment Score} = 1 + \text{Weighted Sentiment Score per Video}
$$

$$
\text{Cluster Boost} = 1.2
$$


---

## **Project Schema**:

![flowchart_diagram_dark](https://github.com/user-attachments/assets/547f55b6-96f5-4e37-8ca7-794ba83e1192)

---

## Folder structure

```
Sentiment-Driven-Video-Recommendations/
├── assets/                                           # Auxiliary files and resources (e.g., images for documentation)
├── data/                                             # Data folder
│   ├── clean/                                        # Data from Sentiment Analysis through PySpark
│   ├── clean_data/                                   # Processed data 
│   ├── raw_data/                                     # Unprocessed, original data from Youtube API
│   └── README.md                                     # Explanation of the data folder contents
├── docker_app/                                       # Docker-related files and application code
│   ├── __pycache__/                                  # Python cache for compiled files
│   ├── Dockerfile                                    # Instructions for building the Docker image
│   ├── final_score_matrix.joblib                     # Precomputed final score matrix for recommendations
│   ├── main_app.py                                   # Main application script
│   ├── readme.rst                                    # Documentation for Docker app setup
│   └── requirements.txt                              # Python dependencies for the project
└── notebooks/                                        # Jupyter notebooks for analysis and modeling
    ├── 0_fetch_and_clean_data_youtube_api.ipynb      # Fetch and clean data from YouTube API
    ├── 2_emotion_analysis_pyspark.ipynb              # Perform sentiment analysis using PySpark
    ├── 3_clustering.ipynb                            # Clustering analysis for video grouping
    └── 4_tfidf_matrix_and_model_pipeline.ipynb       # Build TF-IDF matrix and model pipeline

```

-----------------------------------------------------------------------------------------------------------------

# **Key Features**

## 1️⃣ **Content-Based Filtering**:
- Built a **TF-IDF matrix** from video transcriptions.

$$
\text{TF}(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d}
$$

$$
\text{IDF}(t) = \log\left(\frac{N}{|\{d \in D : t \in d\}|}\right)
$$

$$
\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)
$$

- Applied **Cosine Similarity** to identify similar videos.

![final_matrix_triangular](https://github.com/user-attachments/assets/4ee7631b-35e5-418f-a0c0-457ec3967f53)

---

## 2️⃣ **Sentiment-Weighted Recommendations**:
- 💬 Incorporated **sentiment analysis** to refine similarity scores.
- 📊 Integrated video statistics (**view count**, **like count**, **comment count**) into the final recommendation score.

![Sentiment Analysis Visualization](https://github.com/user-attachments/assets/eb5ca8a8-dc43-4d39-9340-dfd4f85da648)

---

## 3️⃣ **Clustering**:
- **DBSCAN** and **K-MEANS** for clustering videos based on their features.
- Prioritized videos from the same cluster in the recommendation process.

![video_clustering_kmeans](https://github.com/user-attachments/assets/fc4c6798-96c8-43d6-a216-313b148df6b6)

---

# **Data**

## **Datasets from YouTube API**
Conducted research through the **YouTube API** with queries about 'Artificial Intelligence':

- "What is artificial intelligence?"
- "Artificial intelligence applications in healthcare"
- "AI in autonomous vehicles"
- "Machine learning vs deep learning"
- "Artificial intelligence in finance"
- "How does AI work?"
- "Top AI tools for data science"
- "Artificial intelligence in robotics"

### **Gathered Datasets:**

- **`df_videos`**: Video data including **view count**, **like count**, **comment count**, and more.
  
- **`df_comments`**: Comment data with **sentiment analysis** and engagement metrics.

- **`df_channels`**: Channel-level data including **subscriber count** and total video views.
  
- **`df_categories`**: Categorical data related to video genres and types.

![Entity-Relationship Diagram](https://github.com/user-attachments/assets/072ef07f-c14f-4c7e-95df-4c159d9da5ab)

## Technologies Used
 - Python, PySpark
 - Natural Language Processing (NLTK, Google Translate)
 - Machine Learning (RoBERTa LLM, TF-IDF, K-Means, DBScan, PCA)
 - Docker
 - FastAPI
 - Google Cloud (Cloud Storage, Cloud Run)

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/ivanseldas/Sentiment-Driven-Video-Recommendations.git
```

### 2. Navigate to the project directory:
```bash
cd Sentiment-Driven-Video-Recommendations
```

## Future Work

- **Precision@K, Recall@K, F1-Score**: The recommendation system achieves high relevance in its top-K recommendations, indicating a well-tuned model.
- **Clustering Insights**: The DBSCAN clustering effectively groups similar videos, enhancing the recommendation diversity.
- **Explore Supervised Learning**: Implement supervised models for further improving recommendation accuracy.
- **A/B Testing**: Deploy the system in a real-world setting for user feedback and further refinement.
- **Scalability**: Optimize the system for larger datasets and real-time recommendations.

## Contributors

- **Ivan Seldas Perulero**

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
