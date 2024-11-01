# **Sentiment-Driven Video Recommendations**
[Link to project](https://video-recommendation-project-321465604500.us-central1.run.app/)

YoutubeAPI | Google Cloud | PySpark | NLP | Huggingface | DBScan | K-Means

[End-to-end] Personalized video recommendation system based on **video content**, **user interactions**, and **sentiment analysis** from comments to recommend relevant videos to users.

![image](https://github.com/user-attachments/assets/aed6ff86-d0df-47c3-a137-39b8511a6034)

---

## **Input:**

| <span style="color:#ff6347">**video_id**</span> | <span style="color:#ff6347">**title**</span> |
|:------------|:--------------------------------------|
| **Z5s4cWbZX6E** | **The Ethics of Artificial Intelligence** |

---

## **Top 5 Recommendations**

| <span style="color:#4682b4">**video_id**</span> | <span style="color:#4682b4">**title**</span> | <span style="color:#4682b4">**final_score**</span> |
|:------------|:-------------------------------------------------------------------------------|--------------:|
| **Aof4BxK0UlY** | Artificial Intelligence Advances, and the Ethical Choices Ahead                |       **1.36436** |
| **kX4oTF-2_kM** | #12np:  Artificial Intelligence is Hard to See: Social & ethical impacts of AI |       **1.30757** |
| **7Azhgh0nhBY** | Artificial Intelligence: How It Will Impact the Financial Industry             |       **1.2211**  |
| **AT8JCkJH9pY** | The Future of Artificial Intelligence - Shaping our AI Futures                 |       **1.1094**  |
| **yIRL4xtmXE4** | How Will Artificial Intelligence Change Ethics? - Pedro Domingos               |       **1.10072** |

---

## **Final Score Calculation:**

$$
\text{Final Score} = \text{Cosine Similarity Matrix} \times \text{Sentiment Score} \times \text{Cluster Boost}
$$

where:

- **Cosine Similarity Matrix** from the video transcripts.

- **Sentiment Score** from the video comments, defined as:

$$
\text{Sentiment Score} = 1 + \text{Weighted Sentiment}
$$

- **Cluster Boost** from the videos with similar stats, defined as constant when belogning to same cluster:

$$
\text{Cluster Boost} = 1.2
$$


![flowchart_diagram_dark](https://github.com/user-attachments/assets/547f55b6-96f5-4e37-8ca7-794ba83e1192)


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
Conducted research through the **YouTube API** with 5 queries about 'Artificial Intelligence':

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

## Project structure

```
video_recommender_project/
│
├── app/
│   ├── __init__.py
│   ├── api.py               # FastAPI app to serve recommendations
│   ├── recommender.py       # Logic to load and query the precomputed matrix
│   ├── preprocessing.py     # Preprocessing for TF-IDF, sentiment analysis, clustering, and generating the final matrix
│   ├── data_loader.py       # Load and store DataFrames (df_videos and df_comments)
│   └── utils.py             # Auxiliary functions
│
├── data/
│   ├── df_videos.csv        # DataFrame with video information
│   ├── df_comments.csv      # DataFrame with video comments
│   └── final_score_matrix   # Precomputed final score matrix
│
├── Dockerfile               # Docker container definition
├── requirements.txt         # Project dependencies (FastAPI, NumPy, scikit-learn, etc.)
├── preprocess_final_matrix.py # Script to precompute the final matrix
└── README.md                # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
