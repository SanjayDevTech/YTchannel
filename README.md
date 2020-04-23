# YTchannel
YouTube channel & video details extractor

## Features
Retrieve:-
- Youtube Video downloader
- Youtube Channel details
- Youtube Video details

## Requirements
You need to install requests module
```
pip install requests
```

## Installation
```
pip install YTchannel
```

## Importing
```python
import YTchannel as yt
```


## To Download Videos
```python
download = yt.YTdownloader()
```
#### Initialize video extraction
```python
try:
  download.startDownload(video_url=video_url,video_id = video_id)
except KeyError:
  #Invalid video id
except ConnectionError:
  #Connection error
except IndexError:
  #Can't find video
except:
  #Something went wrong
```
#### Get Result
```python
result = download.getResults()
```


## For Channel details
```python
channel = yt.Channel()
```
#### Calling with a Id and API key
The first parameter must be the Channel id
Check below example
https://www.youtube.com/channel/UC_channel_id
here in this example the channel id is **UC_channel_id**
```python
try:
  channel.startChannel(UC_channel_id,YOUR_API_KEY)
except KeyError:
  #Invalid channel id
except ConnectionError:
  #Connection error
except:
  #Something went wrong
```
#### Check if the request is success
```python
result = channel.getChannel() #this will return all details in a dictionary
if result['result'] == 'OK':
  #No problem do your thing
else:
  #Something wrong like - no channel found or invalid api key
  #use result['code'] to get the error code or result['message'] to know the message
```
#### How to get details
```python
print(result) #this will print all the details of a channel in a dictionary
```


## For video details
```python
video = yt.Video()
```
#### Calling with a Id and API key
The first parameter must be the video id or video_url
Check below example
https://www.youtube.com/watch?v=video_id
here in this example the video id is **video_id**
```python
try:
  video.startVideo(video_url=video_url,video_id = video_id,YOUR_API_KEY)
except KeyError:
  #Invalid video id
except ConnectionError:
  #Connection error
except:
  #Something went wrong
```
#### Check if the request is success
```python
resultVideo = video.getVideo() #this will return all details in a dictionary
if resultVideo['result'] == 'OK':
  #No problem do your thing
else:
  #Something wrong like - no video found or invalid api key
  #use resultVideo['code'] to get the error code or resultVideo['message'] to know the message
```
#### How to get details
```python
print(resultVideo) #this will print all the details of a video in a dictionary
```

## Any issues?
Create an issue on github

## Contact me
- On twitter https://twitter.com/SanjayDevTech


# **Happy coding**

