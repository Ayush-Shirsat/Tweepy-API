# Mini_Proj_1: Learning APIs
Downloads images from a twitter feed and converts them to a video using FFMPEG. The contents of this video are analyzed using Google Cloud Video Intelligence API.

# Built using
*Python 3.6.5*

*ffmpeg 3.4.4*

*Tweepy 3.6.0*

*google-cloud-videointelligence 1.3.0*

*Ubuntu 18.04.1 LTS*

# How the program works

**Step-1:**

Run the program "Main_code.py"
Make sure that a file containing twitter credentials is imported as shown in line: 8. File "twitter_credentials.py" has the necessary credentials required to run.
This program uses streaming class of tweepy. A track name is set on line:38 and the program starts loading tweets based on the track. Tweet limit is set to 200 tweets which can be altered by changing the value on line: 18.
All tweets are in json format and get saved in a file named "fetched_tweets.json". I have decided to stream tweets as it gives me a wider range of options than user handle. 

**Step-2:**

Run the program "get_images.py"
This program reads the contents of file "fetched_tweets.json" created in Step-1. 
It looks for the keyword 'Media_url'.
If Media_url is found, the program prints 'Yes' and the Media URL.
If Media_url is not found, the program prints 'No'.
All images are saved as 'imgxxxx.jpg'.

**Step-3:**

Run the program "to_video.py"
This program uses FFMPEG to convert images to video.
Frame rate is set to 1 fps.
Video is saved as '.mp4' file.

**Step-4:**

Run the program "vid_analysis.py"
This program uses Google Cloud Video Intelligence API to categorize the contents of the video.
It outputs the category and its confidence.

# Bugs/ Errors
Sometimes file "vid_analysis.py" throws an error about google application credentials. To fix that run the following command on terminal:

```
export GOOGLE_APPLICATION_CREDENTIALS='google_application_credentials.json'
```
Make sure file 'google_application_credentials.json' has correct path.

# Conclusion

Tweepy was used to stream tweets and save them to a file in .json format. Media URLs were extracted from tweets that had media images in them. FFMPEG was used to convert these images to video with frame rate of 1 fps. This video was analyzed using Google Cloud Video Intelligence API. Content of video was categorized and confidence was printed. Errors and exceptions were also taken into account. 
