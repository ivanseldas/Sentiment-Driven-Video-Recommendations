# 🎯 **Sentiment-Driven Video Recommendations** 🎯

Personalized video recommendation system based on **video content**, **user interactions**, and **sentiment analysis** from comments to recommend relevant videos to users.

---

## **🎥 Input:**

| <span style="color:#ff6347">**video_id**</span> | <span style="color:#ff6347">**title**</span> |
|:------------|:--------------------------------------|
| **Z5s4cWbZX6E** | **The Ethics of Artificial Intelligence** |

---

## **🔝 Top 5 Recommendations**

| <span style="color:#4682b4">**video_id**</span> | <span style="color:#4682b4">**title**</span> | <span style="color:#4682b4">**final_score**</span> |
|:------------|:-------------------------------------------------------------------------------|--------------:|
| **Aof4BxK0UlY** | Artificial Intelligence Advances, and the Ethical Choices Ahead                |       **1.36436** |
| **kX4oTF-2_kM** | #12np:  Artificial Intelligence is Hard to See: Social & ethical impacts of AI |       **1.30757** |
| **7Azhgh0nhBY** | Artificial Intelligence: How It Will Impact the Financial Industry             |       **1.2211**  |
| **AT8JCkJH9pY** | The Future of Artificial Intelligence - Shaping our AI Futures                 |       **1.1094**  |
| **yIRL4xtmXE4** | How Will Artificial Intelligence Change Ethics? - Pedro Domingos               |       **1.10072** |

---

## **🔍 Recommendations based on:**

- **📹 Video Content**: Creating a similarity matrix from the video transcripts.
- **💬 Comments Sentiment Analysis**: Extracting the sentiments of each video for more personalized recommendations.
- **🔗 Clustering**: Clustering similar videos based on their figures and applying these clusters in the recommendation process.


-----------------------------------------------------------------------------------------------------------------

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

### Data
## Datasets from YouTube API
Decided to do research through the API with 5 queries about 'Artificial Intelligence':

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

![EDR](https://github.com/user-attachments/assets/072ef07f-c14f-4c7e-95df-4c159d9da5ab)


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

## Results

- **Precision@K, Recall@K, F1-Score**: The recommendation system achieves high relevance in its top-K recommendations, indicating a well-tuned model.
- **Clustering Insights**: The DBSCAN clustering effectively groups similar videos, enhancing the recommendation diversity.

## Future Work

- **Explore Supervised Learning**: Implement supervised models for further improving recommendation accuracy.
- **A/B Testing**: Deploy the system in a real-world setting for user feedback and further refinement.
- **Scalability**: Optimize the system for larger datasets and real-time recommendations.

## Contributors

- **Ivan Seldas Perulero**

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
