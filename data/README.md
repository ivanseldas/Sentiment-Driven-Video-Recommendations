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

- **videoId:** `qtlUwwtvuEg`
- **title:** "2024 Twelve Best free AI tools for Academic Research"
- **publishedAt:** "2023-05-01T13:00:18Z"
- **viewCount:** 268,029
- **likeCount:** 8,091
- **commentCount:** 381
- **duration:** 1499 seconds (approximately 25 minutes)
- **language:** "en" (English)



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
