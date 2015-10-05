import requests
import time
import re

KEY='AIzaSyCeIG1Ln9FUV8ss3rOs-levMlBKAC6urPU'

############
def getVideoData(vid):
############
    '''Takes vide ID (str) and gets full video info from API.'''
    requestUrl='https://gdata.youtube.com/feeds/api/videos/'+vid+'?v=2&alt=json'
    requestUrl='https://www.googleapis.com/youtube/v3/videos?part=id&id='+vid+'&key='+KEY
    d=requests.get(requestUrl)
       
#    print requestUrl
              
    nTries=0

    while not d.status_code==200:
        print d.text
                              
        if re.search(r'too_many_recent_calls',d.text):
            print 'API THRASHED. SLEEPING...'
            time.sleep(60)
            print 'RETRYING'
            d=requests.get(requestUrl)
            print 'GOT CODE',d.status_code

        if nTries==10 or re.search('Video not found|Private video|ServiceUnavailableException',d.text):
            print 'GIVING UP',vid
            return {'videoId':vid,'missing':[int(time.time())]}
        nTries+=1
    return d.json()

