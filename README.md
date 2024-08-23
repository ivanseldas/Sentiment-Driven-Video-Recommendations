# Sentiment-Driven Video Recommendations
Personalized video recommendation system based on video content, user interactions, and sentiment analysis from comments to recommend relevant videos to users.

-----------------------------------------------------------------------------------------------------------------

                            
![waiting_temp](https://github.com/user-attachments/assets/509d4d0f-eb6f-4b8a-a4fb-81f0d2eddef4)


-----------------------------------------------------------------------------------------------------------------

## Recommendations based on:

- **Video Content**: creating a similarity cousine matrix from the video transcripts.
- **Comments Sentiment Analysis**: extracting the sentiments of each video for more personalized recommendations.
- **Clustering**: clustering similar videos based on their figures  and applying these clusters in the recommendation process.

## Key Features

### 1. Content-Based Filtering:
- Built a TF-IDF matrix from video transcriptions.

$$
\text{TF}(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d}
$$

$$
\text{IDF}(t) = \log\left(\frac{N}{|\{d \in D : t \in d\}|}\right)
$$

$$
\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)
$$

- Applied cosine similarity to identify similar videos.

![image](https://github.com/user-attachments/assets/e3e29e7b-5629-454a-831a-19cd82bb12c4)


### 2. Sentiment-Weighted Recommendations:
- Incorporated sentiment analysis to refine similarity scores.
- Integrated video statistics (view count, like count, comment count) into the final recommendation score.

![image](https://github.com/user-attachments/assets/eb5ca8a8-dc43-4d39-9340-dfd4f85da648)


### 3. Clustering:
- Applied DBSCAN for clustering videos based on their features.
- Prioritized videos from the same cluster in the recommendation process.

![image](https://github.com/user-attachments/assets/b202fc96-22af-4fdf-a2da-cbaecbd0be52)


## How It Works

### 1. Data Preparation:
- Cleaned and standardized video and comment data.
- Applied sentiment analysis.
- Engineered relevant features.

### 2. Recommendation Generation:
- Generated recommendations using TF-IDF and cosine similarity.
- Adjusted recommendations based on sentiment and video statistics.
- Boosted recommendations from the same cluster and ensured language consistency.

### 3. Evaluation:
- Used Precision@K, Recall@K, and F1-Score to evaluate recommendation quality.
- Applied the Silhouette Score for cluster validation.

### Data
## Datasets from Youtube API
Decided to do a research through the API with 5 queries about 'Artificial Intelligence':

- "What is artificial intelligence?"
- "Artificial intelligence applications in healthcare"
- "AI in autonomous vehicles"
- "Machine learning vs deep learning"
- "Artificial intelligence in finance"
- "How does AI work?"
- "Top AI tools for data science"
- "Artificial intelligence in robotics"

The following datasets were gathered:

- **`df_videos`**: Video data including view count, like count, comment count, and more.
  
- **`df_comments`**: Comment data with sentiment analysis and engagement metrics.

- **`df_channels`**: Channel-level data including subscriber count and total video views.
  
- **`df_categories`**: Categorical data related to video genres and types.

![EDR](https://github.com/user-attachments/assets/8922dff4-4cbe-4d00-90a0-e9037fc39fc7)



## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/ivanseldas/Sentiment-Driven-Video-Recommendations.git
```

### 2. Navigate to the project directory:
```bash
cd Sentiment-Driven-Video-Recommendations
```

### 3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Data Preparation:
- Load and clean the datasets.
- Run the feature engineering scripts to generate additional features.

### 2. Generate Recommendations:
- Use the provided functions to recommend videos based on a given video ID.
- Adjust parameters such as `boost_factor` to refine recommendations.

### 3. Evaluate Model:
- Run evaluation scripts to assess model performance using various metrics.

## Results

- **Precision@K, Recall@K, F1-Score**: The recommendation system achieves high relevance in its top-K recommendations, indicating a well-tuned model.
- **Clustering Insights**: The DBSCAN clustering effectively groups similar videos, enhancing the recommendation diversity.

## Future Work

- **Explore Supervised Learning**: Implement supervised models for further improving recommendation accuracy.
- **A/B Testing**: Deploy the system in a real-world setting for user feedback and further refinement.
- **Scalability**: Optimize the system for larger datasets and real-time recommendation.

## Contributors

- **Ivan Seldas Perulero**

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
