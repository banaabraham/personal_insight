import tweepy
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

def analyze(handle):
    
    CONSUMER_KEY='jHpNFh0Hi12ECGEWdtKM3aTAm'
    CONSUMER_SECRET='FfeyjmMCUKQRvNBmgRcNU7h51paOPLbU8yM7cNjOwoJ7GkwykM'
    OAUTH_TOKEN='880785141940928514-EDFIfnfzeIDMSj3jbGJeLHYiKpw2m4C'
    OAUTH_TOKEN_SECRET='BMmIsrCDAI2GHwk2043M53jxaSrExNh7CyoFBg4rXqTCY'
     
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tweepy.API(auth)
    print (api) 
    
    statuses = api.user_timeline(screen_name = handle, count=100)
   
    
    text = ""
    for status in statuses:
        text += (status._json)['text']
    
    pi_username = '14a6ca18-57af-4476-8bfa-220137ce47ce'
    pi_password = '6yKmqNTH3rGw'
    
    personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
    pi_result = personality_insights.profile(text)
    return pi_result


def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data
  
def compare(dict1, dict2):
   compared_data = {}
   for keys in dict1:
       if dict1[keys] != dict2[keys]:
         compared_data[keys]=abs(dict1[keys] - dict2[keys])
   return compared_data
  
user_handle= '@ganjarputro'
  
user_result = analyze(user_handle)
  
user = flatten(user_result)

print("user: %s" %(user_handle))
for k in user.keys():
    print ("%s -> %f" %(k,user[k]*100))
