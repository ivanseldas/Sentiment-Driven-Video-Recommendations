## YouTube Data Fetched from API

## `df_videos`:
This dataset contains detailed information about various YouTube videos, specifically those related to artificial intelligence and similar technologies. Each row in the dataset represents a unique video and provides a variety of associated metadata.

### Main Columns:

- **videoId:** Unique identifier for the video on YouTube.
- **title:** Title of the video.
- **channelId:** Unique identifier for the channel that uploaded the video.
- **description:** Description of the video provided by the author.
- **publishedAt:** Date and time when the video was published, in ISO 8601 format.
- **thumbnail_url:** URL of the video’s thumbnail.
- **tags:** List of tags associated with the video, indicative of its content and theme.
- **categoryId:** Identifier of the video’s category according to YouTube’s classification.
- **viewCount:** Number of views the video has received.
- **likeCount:** Number of likes the video has received.
- **commentCount:** Number of comments made on the video.
- **licensed:** Indicates whether the video contains licensed content (True/False).
- **duration:** Duration of the video in seconds.
- **caption:** Indicates if the video has captions available (True/False).
- **language:** Primary language of the video.

### Data Examples:

- **videoId:** `qtlUwwtvuEg`
- **title:** "2024 Twelve Best free AI tools for Academic Research"
- **publishedAt:** "2023-05-01T13:00:18Z"
- **viewCount:** 268,029
- **likeCount:** 8,091
- **commentCount:** 381
- **duration:** 1499 seconds (approximately 25 minutes)
- **language:** "en" (English)

### Data columns (total 15 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   videoId        2711 non-null   object
 1   title          2711 non-null   object
 2   channelId      2711 non-null   object
 3   description    2535 non-null   object
 4   publishedAt    2711 non-null   object
 5   thumbnail_url  2711 non-null   object
 6   tags           2711 non-null   object
 7   categoryId     2711 non-null   int64 
 8   viewCount      2711 non-null   int64 
 9   likeCount      2711 non-null   int64 
 10  commentCount   2711 non-null   int64 
 11  licensed       2711 non-null   bool  
 12  duration       2711 non-null   int64 
 13  caption        2711 non-null   bool  
 14  language       2711 non-null   object
dtypes: bool(2), int64(5), object(8)

This dataset is useful for analyzing trends in content related to artificial intelligence on YouTube, including popularity, user engagement (likes, comments), and how these videos are distributed across different categories.
