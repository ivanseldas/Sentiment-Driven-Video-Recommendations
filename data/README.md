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

### Code:

```
# Function to fetch video metadata
def fetch_video_metadata(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&id={video_id}&key={api_key}"
    response = requests.get(url).json()
    if 'items' in response and len(response['items']) > 0:
        return(response['items'])
    else:
        return None
```

## `df_transcript`:

## Main Columns

- **video_id:** Unique identifier for the video on YouTube.
- **transcription:** The textual transcription of the spoken content in the video.
- **language:** The language in which the transcription is written.
- **translation:** The translated version of the transcription, if available.

## Data Examples

- **video_id:** `3qGbPDRzYRI`

  - **transcription:** "hi i'm nick romano ceo of deeplight thanks for..."
  - **language:** `english`
  - **translation:** `NaN` (No translation available)

- **video_id:** `K2tXKfKhryo`

  - **transcription:** "यह बिल्कुल वाकई बीटेक कंप्यूटर साइंस फिक्शन क..."
  - **language:** `hindi`
  - **translation:** "This is absolutely really B.Tech computer science fiction..."

- **video_id:** `3Rb2hRf5YCQ`

  - **transcription:** "[Música] y sí a ella [Aplausos] aquí no el lib..."
  - **language:** `spanish`
  - **translation:** "[Music] and yes to her [Applause] here not the..."


| video_id   | transcription                                                           | language | translation                                                    |
|------------|-------------------------------------------------------------------------|----------|----------------------------------------------------------------|
| 3qGbPDRzYRI| hi i'm nick romano ceo of deeplight thanks for...                        | english  | NaN                                                            |
| Amfrm2V_KO0| [Music] how much learning material can you ret...                        | english  | NaN                                                            |
| K2tXKfKhryo| यह बिल्कुल वाकई बीटेक कंप्यूटर साइंस फिक्शन क...                         | hindi    | This is absolutely really B.Tech computer science fiction...    |
| 3Rb2hRf5YCQ| [Música] y sí a ella [Aplausos] aquí no el lib...                        | spanish  | [Music] and yes to her [Applause] here not the...               |
| Rp7qqjlBeRY| morning or good afternoon or good evening depending on your time zone... | english  | NaN                                                            |

