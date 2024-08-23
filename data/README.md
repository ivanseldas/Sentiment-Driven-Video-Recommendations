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

|    | videoId     | title                                                                                                | publishedAt          |   categoryId |   viewCount |   likeCount |   commentCount |   duration |
|---:|:------------|:-----------------------------------------------------------------------------------------------------|:---------------------|-------------:|------------:|------------:|---------------:|-----------:|
|  0 | qtlUwwtvuEg | 2024 Twelve Best free AI tools for Academic Research || Latest AI tools || AI for researchers        | 2023-05-01T13:00:18Z |           27 |      268029 |        8091 |            381 |       1499 |
|  1 | QaoDXYYtgK0 | Facebook A.I. Robots shut down after creating their own language |Artificial Intelligence |#facebook | 2017-07-31T23:32:53Z |           24 |     3369370 |       35258 |           5948 |        159 |
|  2 | PqDwddEHswU | Why Choose Deep Learning? | Deep Learning for Engineers, Part 1                                      | 2021-04-13T13:15:02Z |           28 |      143984 |        2575 |             36 |        883 |
|  3 | B-Y7rnOa43w | Earn thousands of dollars per day with A.I passively! #artificialintelligence #passiveincome         | 2023-04-07T13:39:48Z |           28 |        2430 |         270 |              3 |         44 |
|  4 | vyit-1zKsZ4 | Doctors, apps and artificial intelligence - The future of medicine | DW Documentary                  | 2022-12-13T17:00:35Z |           27 |      113233 |        2030 |             84 |       1706 |   

This dataset is useful for analyzing trends in content related to artificial intelligence on YouTube, including popularity, user engagement (likes, comments), and how these videos are distributed across different categories.
