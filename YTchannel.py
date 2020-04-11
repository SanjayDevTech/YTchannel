import requests

class YTchannel:
    def __init__(self):
        self.title = ''
        self.icon = ''
        self.subs = ''
        self.country = None
        self.subhidden = False
        self.videos = ''
        self.des = ''
        self.channelArt = ''
        self.__response = ''
        self.__result = False
        self.__code = 0
        self.__msg = ''
        self.__reason = ''
        self.__extendedHelp = ''
        self.__dictChart = {}
        
        

    def start(self,channel_id,api_key):
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
                    self.icon = self.__json['items'][0]['snippet']['thumbnails']['high']['url']
                    self.channelArt = self.__json['items'][0]['brandingSettings']['image']['bannerImageUrl']
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

    def getResult(self):
        '''This function will return a dictionary of contents'''
        '''It may contain error code if the request failed'''
        self.__dictChart = {}
        if self.__result:
            self.__dictChart['result'] = 'OK'
            self.__dictChart['title'] = self.title
            self.__dictChart['des'] = self.des
            self.__dictChart['icon'] = self.icon
            self.__dictChart['channelArt'] = self.channelArt
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
            
            
