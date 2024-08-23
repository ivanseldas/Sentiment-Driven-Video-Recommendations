
# Sentiment-Driven Video Recommendations

![image](https://github.com/user-attachments/assets/a8b302c5-e168-4a00-a6b6-a1fbcae83a7f)

## Project Overview

Personalized video recommendation system based on video content, user interactions, and sentiment analysis from comments to recommend relevant videos to users.

## Objectives

- **Develop a Recommendation System**: Create a system that recommends videos based on content similarity, sentiment analysis, and video statistics.
- **Incorporate Sentiment Analysis**: Adjust recommendations using sentiment data extracted from user comments.
- **Utilize Clustering**: Enhance recommendations by clustering similar videos and applying these clusters in the recommendation process.

## Datasets

- **`df_videos`**: Video data including view count, like count, comment count, and more.
  
- **`df_comments`**: Comment data with sentiment analysis and engagement metrics.

|    | comment_id                 | text                                                                                               |   like_count | published_at              |
|---:|:---------------------------|:---------------------------------------------------------------------------------------------------|-------------:|:--------------------------|
|  0 | UgxqJ2eO2p7w2NEvB2p4AaABAg | great video,helpful.                                                                               |            1 | 2024-08-17 13:07:48+00:00 |
|  1 | UgzmXwaNzivNHqjfR5l4AaABAg | Thank you for such well explained video tutorial                                                   |            4 | 2023-05-01 14:48:21+00:00 |
|  2 | UgyySzt4xOZ1hKdS97x4AaABAg | very useful tools , thanks for sharing this info with us.                                          |            2 | 2023-07-20 11:33:23+00:00 |
|  3 | UgyHVo-IOZw_-uLb-wh4AaABAg | This is great information and a terrific use of AI. Thanks for creating this video and posting it. |           13 | 2023-06-25 00:36:50+00:00 |
|  4 | UgyIT65ucXCc-4loBEx4AaABAg | first two are not goof but all other AI id the best thanks for sharing this video                  |            1 | 2023-05-31 16:41:21+00:00 |

- **`df_channels`**: Channel-level data including subscriber count and total video views.
  
- **`df_categories`**: Categorical data related to video genres and types.

## Key Features

### 1. Content-Based Filtering:
- Built a TF-IDF matrix from video transcriptions.

$$
\text{TF}(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d}
$$

- Applied cosine similarity to identify similar videos.

### 2. Sentiment-Weighted Recommendations:
- Incorporated sentiment analysis to refine similarity scores.
- Integrated video statistics (view count, like count, comment count) into the final recommendation score.

### 3. Clustering:
- Applied DBSCAN for clustering videos based on their features.
- Prioritized videos from the same cluster in the recommendation process.

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
