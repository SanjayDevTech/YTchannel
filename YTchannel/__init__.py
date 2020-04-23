import requests,urllib.parse,re,sys


class YTdownloader:
    __pattern = r"^(?:http(?:s)?:\/\/)?(?:www\.)?(?:m\.)?(?:youtu\.be\/|youtube\.com\/(?:(?:watch)?\?(?:.*&)?v(?:i)?=|(?:embed)\/))([^\?&\"'>]+)"
    def __init__(self):
        self.__video_id = ''
        self.__URL = ''
        self.results = []

    def startDownload(self,video_url=None,video_id=None):
        if video_url == None and video_id == None:
            raise KeyError('Invalid parameter')
        elif video_url ==None:
            self.__video_id = video_id
        elif video_id == None:
            res =re.search(YTdownloader.__pattern,video_url)
            if res == None:
                raise KeyError('Invalid Url')
        self.__video_id = res[1]
        self.__URL = "https://www.youtube.com/get_video_info?video_id="+res[1]+"&cpn=CouQulsSRICzWn5E&eurl&el=adunit"
        try:
            self.__response = requests.get(self.__URL)
        except:
            raise ConnectionError("Something went wrong")
        else:
            if self.__response.status_code != 200:
                raise ConnectionError('Bad Request')
            else:
                self.__data = urllib.parse.parse_qs(self.__response.text)
                self.__videoData = eval(self.__data['player_response'][0].replace(":true",":True").replace(":false",":False"))
                if 'streamingData' not in self.__videoData:
                    raise KeyError("Can't find video")
                self.__streamingData = self.__videoData['streamingData']
                self.__streamingDataFormats = self.__streamingData['formats'];
                self.results = []
                for self.__formats in self.__streamingDataFormats:
                    self.results.append(self.__formats)
    def getResults(self):
        return self.results

class Video:
    __pattern = r"^(?:http(?:s)?:\/\/)?(?:www\.)?(?:m\.)?(?:youtu\.be\/|youtube\.com\/(?:(?:watch)?\?(?:.*&)?v(?:i)?=|(?:embed)\/))([^\?&\"'>]+)"
    def __init__(self):
        self.title = ''
        self.thumbnails = ''
        self.channelId = ''
        self.des = ''
        self.publishedAt = ''
        self.channelTitle = ''
        self.viewCount = ''
        self.likeCount = ''
        self.dislikeCount = ''
        self.commentCount = ''
        self.__response = ''
        self.__result = False
        self.__code = 0
        self.__msg = ''
        self.__reason = ''
        self.__extendedHelp = ''
        self.__dictChart = {}
    
    def startVideo(self,api_key,video_url=None,video_id=None):
        if video_url == None and video_id == None:
            raise KeyError('Invalid parameter')
        elif video_url ==None:
            self.video_id = video_id
        elif video_id == None:
            res =re.search(YTdownloader.__pattern,video_url)
            if res == None:
                raise KeyError('Invalid Url')
        self.video_id = video_id
        self.api = api_key
        self.__URL ='https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id='+self.video_id+'&key='+self.api
        try:
            self.__response = requests.get(self.__URL)

        except:
            raise ConnectionError("Something went wrong")
            

        else:
            
            self.__json = self.__response.json()
            if 'error' not in self.__json:
                if int(self.__json['pageInfo']['totalResults']) > 0:
                    self.__result = True
                    self.title = self.__json['items'][0]['snippet']['title']
                    self.des = self.__json['items'][0]['snippet']['description']
                    self.thumbnails = self.__json['items'][0]['snippet']['thumbnails']
                    self.channelId = self.__json['items'][0]['snippet']['channelId']
                    self.publishedAt = self.__json['items'][0]['snippet']['publishedAt']
                    self.channelTitle = self.__json['items'][0]['snippet']['channelTitle']
                    self.viewCount = self.__json['items'][0]['statistics']['viewCount']
                    self.commentCount = self.__json['items'][0]['statistics']['commentCount']
                    self.likeCount = self.__json['items'][0]['statistics']['likeCount']
                    self.dislikeCount = self.__json['items'][0]['statistics']['dislikeCount']
                    

                else:
                    self.__code = 0
                    self.__msg = 'Please check your video id'
                    self.__reason = 'emptyResult'
                    self.__extendedHelp = ''
                    
                
            else:
                self.__code = int(self.__json['error']['code'])
                self.__msg = self.__json['error']['message']
                self.__reason = self.__json['error']['errors'][0]['reason']
                self.__extendedHelp = 'Use this link to know the meaning of the error code:- https://developers.google.com/youtube/v3/docs/videos/list?hl=en-US#errors_1'
                
    def getVideo(self):
        '''This function will return a dictionary of contents'''
        '''It may contain error code if the request failed'''
        self.__dictChart = {}
        if self.__result:
            self.__dictChart['result'] = 'OK'
            self.__dictChart['title'] = self.title
            self.__dictChart['des'] = self.des
            self.__dictChart['thumbnails'] = self.thumbnails
            self.__dictChart['channelId'] = self.channelId
            self.__dictChart['publishedAt'] = self.publishedAt
            self.__dictChart['channelTitle'] = self.channelTitle
            self.__dictChart['viewCount'] = self.viewCount
            self.__dictChart['commentCount'] = self.commentCount
            self.__dictChart['likeCount'] = self.likeCount
            self.__dictChart['dislikeCount'] = self.dislikeCount
            return self.__dictChart
        else:
            self.__dictChart['result'] = 'FAILURE'
            self.__dictChart['code'] = self.__code
            self.__dictChart['message'] = self.__msg
            self.__dictChart['reason'] = self.__reason
            self.__dictChart['extended_help'] = self.__extendedHelp
            return self.__dictChart

class Channel:
    def __init__(self):
        self.title = ''
        self.icon = ''
        self.subs = ''
        self.country = None
        self.subhidden = False
        self.videos = ''
        self.des = ''
        self.publishedAt = ''
        self.channelArt = ''
        self.__response = ''
        self.__result = False
        self.__code = 0
        self.__msg = ''
        self.__reason = ''
        self.__extendedHelp = ''
        self.__dictChart = {}
        
        

    def startChannel(self,channel_id,api_key):
        '''Use this to initialise the http request to youtube'''
        if 'www.youtube.com' in channel_id:
            raise KeyError('Enter a valid channel id')
        self.cha_id = channel_id
        self.api = api_key
        self.__URL ='https://www.googleapis.com/youtube/v3/channels?part=brandingSettings,statistics,snippet&id='+self.cha_id+'&key='+self.api
        try:
            self.__response = requests.get(self.__URL)

        except:
            raise ConnectionError("Something went wrong")
            

        else:
            
            self.__json = self.__response.json()
            if 'error' not in self.__json:
                if int(self.__json['pageInfo']['totalResults']) > 0:
                    self.__result = True
                    self.title = self.__json['items'][0]['snippet']['title']
                    self.des = self.__json['items'][0]['snippet']['description']
                    self.publishedAt = self.__json['items'][0]['snippet']['publishedAt']
                    self.icon = self.__json['items'][0]['snippet']['thumbnails']
                    self.channelArt = self.__json['items'][0]['brandingSettings']['image']
                    if self.__json['items'][0]['statistics']['hiddenSubscriberCount'] == 'true':
                        self.subhidden = True
                    self.subs = self.__json['items'][0]['statistics']['subscriberCount']
                    self.videos = self.__json['items'][0]['statistics']['videoCount']
                    if 'country' in self.__json['items'][0]['snippet']:
                        self.country = self.__json['items'][0]['snippet']['country']

                else:
                    self.__code = 0
                    self.__msg = 'Please check your channel id'
                    self.__reason = 'emptyResult'
                    self.__extendedHelp = ''
                    
                
            else:
                self.__code = int(self.__json['error']['code'])
                self.__msg = self.__json['error']['message']
                self.__reason = self.__json['error']['errors'][0]['reason']
                self.__extendedHelp = 'Use this link to know the meaning of the error code:- https://developers.google.com/youtube/v3/docs/channels/list?hl=en-US#errors_1'

    def getChannel(self):
        '''This function will return a dictionary of contents'''
        '''It may contain error code if the request failed'''
        self.__dictChart = {}
        if self.__result:
            self.__dictChart['result'] = 'OK'
            self.__dictChart['title'] = self.title
            self.__dictChart['des'] = self.des
            self.__dictChart['icon'] = self.icon
            self.__dictChart['channelArt'] = self.channelArt
            self.__dictChart['publishedAt'] = self.publishedAt
            self.__dictChart['subs'] = self.subs
            self.__dictChart['videos'] = self.videos
            self.__dictChart['subs_hidden'] = self.subhidden
            self.__dictChart['country'] = self.country
            return self.__dictChart
        else:
            self.__dictChart['result'] = 'FAILURE'
            self.__dictChart['code'] = self.__code
            self.__dictChart['message'] = self.__msg
            self.__dictChart['reason'] = self.__reason
            self.__dictChart['extended_help'] = self.__extendedHelp
            return self.__dictChart
            
            
