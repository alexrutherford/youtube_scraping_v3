#Summary
IPython notebook to grab data from YouTube [API](https://developers.google.com/youtube/v3/)

# Error Codes

e.g.

| Code | Description|
|---------|----------|
| 503 | Backend Error (worth waiting and retrying)|
| 403 | Quota exceeded|

More [here](https://developers.google.com/youtube/v3/docs/errors)


#Description

YouTube offers a free API with a quota. Each request incurs a cost which depends on the type of query being made. More direct queries e.g. ‘give me all the information on this particular video’ are cheaper than general queries e.g. ‘give me all videos from this day’. A typical application has a free quota of 50,000,000 units per day with a limit of 3,000 requests per second per user. This limit is only restrictive for applications that make heavy usage of the API: i.e. if there are multiple users and/or operations such as uploading of videos via the API. Once the per second limit is reached, the API will stop returning data and users must wait roughly 10m to try again.

There is an additional API, the Analytics API, that can retrieve detailed statistics on viewers of a video, but is is only available for the owners of that video. Theoretically, this includes gender, country, age, sharing, engagement and route to engagement (i.e. via Google, a related video).

Ties into Google+ platform, so possibility to get user info from their such as location and gender. Can also scrape profile picture to extract gender.

There appears to be a 2 day delay in videos appearing on API

To retrieve 6 months of data using ~20 seach terms takes approximately 1h and <1% quota. 