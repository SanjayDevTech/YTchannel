# YTchannel
YouTube channel details extractor

### Features
- Retrieve Youtube Channel name
- Icon, Channel art
- Subs if not hidden
- List no. of videos

## Installation
```
pip install YTchannel
```

## Importing
```python
from YTchannel.YTchannel import YTchannel
```

## Creating an Object
```python
yt = YTchannel()
```

## Calling with a Id and API key
The first parameter must be the Channel id
Check below example
https://www.youtube.com/channel/UC_channel_id
here in this example the channel id is **UC_channel_id**
```python
try:
  yt.start(UC_channel_id,YOUR_API_KEY)
except KeyError:
  #Invalid channel id
except ConnectionError:
  #Connection error
except:
  #Something went wrong
```
## Check if the request is success
```python
result = yt.getResult() #this will return all details in a dictionary
if result['result'] == 'OK':
  #No problem do your thing
else:
  #Something wrong like - no channel found or invalid api key
  #use result['code'] to get the error code or result['message'] to know the message
```
## How to get details
```python
title = result['title'] #or use title = yt.title
des = result['des'] #or use des = yt.des
icon = result['icon'] #or use icon = yt.icon
subs = result['subs'] #or use subs = yt.subs
channelArt = result['channelArt'] #or use channelArt = yt.channelArt
videos = result['videos'] #or use videos = yt.videos
subhidden = result['subs_hidden'] #or use subhidden = yt.subhidden
country = result['country'] #or use country = yt.country
```

## Any issues?
Create an issue on github

## Contact me
- On twitter https://twitter.com/SanjayDevTech

**Happy coding**