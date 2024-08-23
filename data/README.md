## YouTube Data Fetched from API

## `df_videos`:
This dataset contains detailed information about various YouTube videos, specifically those related to artificial intelligence and similar technologies. Each row in the dataset represents a unique video and provides a variety of associated metadata.

### Main Columns

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

### Data Examples

| videoId      | title                                                 | channelId              | description                                              | publishedAt           | thumbnail_url                                          | tags                                                                 | categoryId | viewCount | likeCount | commentCount | licensed | duration | caption | language |
|--------------|-------------------------------------------------------|------------------------|----------------------------------------------------------|-----------------------|--------------------------------------------------------|----------------------------------------------------------------------|------------|-----------|-----------|--------------|----------|----------|---------|----------|
| qtlUwwtvuEg  | 2024 Twelve Best free AI tools for Academic Re...      | UC4ay94l73_FLJ_WJkIqLnSw| #aitools #researchpaper #academicwriting #...             | 2023-05-01T13:00:18Z  | https://i.ytimg.com/vi/qtlUwwtvuEg/default.jpg         | ['Education', '2023 Latest AI tools', 'AI for ...                    | 27         | 268029    | 8091      | 381          | True     | 1499     | True    | en       |
| QaoDXYYtgK0  | Facebook A.I. Robots shut down after creating ...      | UCppExM9-xECflxA6FLexKiQ| Facebook has shut down two artificial intellig...         | 2017-07-31T23:32:53Z  | https://i.ytimg.com/vi/QaoDXYYtgK0/default.jpg         | ['Facebook A.I. Robots shut down', 'facebook a...                    | 24         | 3369370   | 35258     | 5948         | False    | 159      | False   | en       |
| PqDwddEHswU  | Why Choose Deep Learning? Deep Learning for ...      | UCgdHSFcXvkN6O3NXvif0-pA| This video introduces deep learning from the p...         | 2021-04-13T13:15:02Z  | https://i.ytimg.com/vi/PqDwddEHswU/default.jpg         | ['MATLAB', 'Simulink', 'MathWorks', '624592559...                    | 28         | 143984    | 2575      | 36           | False    | 883      | True    | en       |
| B-Y7rnOa43w  | Earn thousands of dollars per day with A.I pas...      | UCUFMgUDsqQnWFDBxUbBHR3g| NaN                                                      | 2023-04-07T13:39:48Z  | https://i.ytimg.com/vi/B-Y7rnOa43w/default.jpg         | []                                                                | 28         | 2430      | 270       | 3            | True     | 44       | False   | en       |
| vyit-1zKsZ4  | Doctors, apps and artificial intelligence - Th...      | UCW39zufHfsuGgpLviKh297Q| Artificial intelligence is changing health car...         | 2022-12-13T17:00:35Z  | https://i.ytimg.com/vi/vyit-1zKsZ4/default.jpg         | ['Documentary', 'Documentaries', 'documentarie...                    | 27         | 113233    | 2030      | 84           | True     | 1706     | True    | en       |



## `df_comments`:

### Description of the `df_comments` DataFrame

The `df_comments` DataFrame contains detailed information about user comments on YouTube videos. Each row represents a unique comment and includes various attributes related to the comment's content, author, and metadata.

#### Main Columns

- **comment_id:** Unique identifier for the comment on YouTube.
- **author:** The name or username of the comment's author.
- **author_channel_id:** Unique identifier for the YouTube channel of the comment's author.
- **text:** The full text of the comment.
- **like_count:** The number of likes the comment has received.
- **published_at:** The date and time when the comment was originally posted, provided in ISO 8601 format.
- **updated_at:** The date and time when the comment was last updated, if applicable, in ISO 8601 format.
- **totalReplyCount:** The total number of replies to the comment.
- **video_id:** The unique identifier of the YouTube video to which the comment was posted.
- **translation:** The translated version of the comment text, if available.
- **clean_text:** A cleaned version of the comment text, typically used for analysis (e.g., removing special characters or stopwords).
- **sentiment:** A numerical score representing the sentiment of the comment, where higher values indicate more positive sentiment.

This DataFrame is useful for analyzing user engagement and sentiment on YouTube videos, tracking comment activity, and understanding the audience's response to content.

### Data Examples

| comment_id                     | author                  | author_channel_id                    | text                                                         | like_count | published_at                     | updated_at                       | totalReplyCount | video_id     | translation                                                | clean_text                              | sentiment |
|--------------------------------|-------------------------|--------------------------------------|--------------------------------------------------------------|------------|----------------------------------|----------------------------------|----------------|--------------|-------------------------------------------------------------|------------------------------------------|-----------|
| UgxqJ2eO2p7w2NEvB2p4AaABAg     | @emmanuelamama1991      | UCdUooL3DTt3Wj0M3xRnAC3Q             | great video,helpful.                                          | 1.0        | 2024-08-17 13:07:48+00:00        | 2024-08-17 13:07:48+00:00        | 1.0            | qtlUwwtvuEg  | great video,helpful.                                        | great videohelpful                       | 0.6249    |
| UgzmXwaNzivNHqjfR5l4AaABAg     | @dr.alexshayo6972       | UCN56M0YoTn18rd_KBFL0QGg             | Thank you for such well explained video tutorial              | 4.0        | 2023-05-01 14:48:21+00:00        | 2023-05-01 14:48:21+00:00        | 1.0            | qtlUwwtvuEg  | Thank you for such well explained video tutorial            | thank well explained video tutorial      | 0.5574    |
| UgyySzt4xOZ1hKdS97x4AaABAg     | @mohdkashif4596         | UCr5Ua5AsmM6phaRu3dBU1qg             | very useful tools , thanks for sharing this in...             | 2.0        | 2023-07-20 11:33:23+00:00        | 2023-07-20 11:33:23+00:00        | 1.0            | qtlUwwtvuEg  | very useful tools , thanks for sharing this in...           | useful tool thanks sharing info u        | 0.8225    |
| UgyHVo-IOZw_-uLb-wh4AaABAg     | @pipedrmmr              | UC5KmDvJCDtoM31gjpGcdYLQ             | This is great information and a terrific use o...             | 13.0       | 2023-06-25 00:36:50+00:00        | 2023-06-25 00:36:50+00:00        | 1.0            | qtlUwwtvuEg  | This is great information and a terrific use o...           | great information terrific use ai thanks creating | 0.9062    |
| UgyIT65ucXCc-4loBEx4AaABAg     | @anamnaz2527            | UCriCWejgmnsDkaX77-Ay8Hw             | first two are not goof but all other AI id the...             | 1.0        | 2023-05-31 16:41:21+00:00        | 2023-05-31 16:41:21+00:00        | 1.0            | qtlUwwtvuEg  | first two are not goof but all other AI id the...           | first two goof ai id best thanks sharing video | 0.8720    |



## `df_transcript`: 
Contains the video transcriptions, as well as their languages and translations if not in English:

## Main Columns

- **video_id:** Unique identifier for the video on YouTube.
- **transcription:** The textual transcription of the spoken content in the video.
- **language:** The language in which the transcription is written.
- **translation:** The translated version of the transcription, if available.

## Data Samples

| video_id   | transcription                                                           | language | translation                                                    |
|------------|-------------------------------------------------------------------------|----------|----------------------------------------------------------------|
| 3qGbPDRzYRI| hi i'm nick romano ceo of deeplight thanks for...                        | english  | NaN                                                            |
| Amfrm2V_KO0| [Music] how much learning material can you ret...                        | english  | NaN                                                            |
| K2tXKfKhryo| यह बिल्कुल वाकई बीटेक कंप्यूटर साइंस फिक्शन क...                         | hindi    | This is absolutely really B.Tech computer science fiction...    |
| 3Rb2hRf5YCQ| [Música] y sí a ella [Aplausos] aquí no el lib...                        | spanish  | [Music] and yes to her [Applause] here not the...               |
| Rp7qqjlBeRY| morning or good afternoon or good evening depending on your time zone... | english  | NaN                                                            |



## `df_channel`:

DataFrame provides detailed information about the YouTube channels of the videos fetched.

### Main Columns

- **channel_id:** Unique identifier for the YouTube channel.
- **title:** The title or name of the YouTube channel.
- **description:** A brief description of the channel’s content and focus.
- **published_at:** The date and time when the channel was created, provided in ISO 8601 format.
- **subscriber_count:** The number of subscribers the channel has.
- **video_count:** The total number of videos uploaded to the channel.
- **view_count:** The total number of views the channel's videos have accumulated.
- **region:** The region or country where the channel is based, represented by a country code.

This DataFrame is useful for analyzing the performance and characteristics of YouTube channels, including their popularity, content focus, and regional distribution.

### Data Examples

| channel_id                       | title                  | description                                                                 | published_at                        | subscriber_count | video_count | view_count | region |
|----------------------------------|------------------------|-----------------------------------------------------------------------------|-------------------------------------|------------------|-------------|------------|--------|
| UCA90OERJunno1mnWL4WrjyQ         | Movies & TV Show Recap | 🎬 Movie Recaps: This channel is dedicated to highlighting key plot points... | 2024-07-17 00:14:17.483317+00:00    | 26               | 53          | 17060      | IL     |
| UCniia-3AGf-HzVXooVcp1lw         | study tips             | My name is Tushar Jaid, thank you for visiting...                            | 2017-08-25 18:24:10+00:00           | 885000           | 596         | 96564487   | IN     |
| UCmFOjlpYEhxf_wJUDuz6xxQ         | John Snow Labs         | Helping healthcare and life science organizations...                        | 2015-12-22 10:11:49+00:00           | 4110             | 452         | 278345     | US     |
| UC8kFF39hsRrFfHM6-7A6APQ         | AI Sciences            | AI Sciences is an e-learning company; the company offers...                 | 2018-10-07 12:08:56+00:00           | 31100            | 371         | 1480785    | US     |
| UCXhQNRQ-eQALFv5Q0ltpOiw         | Knowledge GPT          | Welcome to Knowledge GPT! Our channel is your...                            | 2024-06-07 08:17:39.751713+00:00    | 9                | 45          | 5040       | CA     |
