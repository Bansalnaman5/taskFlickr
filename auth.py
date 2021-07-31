import requests
import requests_oauthlib
from requests_oauthlib import OAuth1

api_key = "b77b2fc41549f6dee570f482b5e2dd77"
api_secret = "09e6f8876673228d"
urlRequestToken = 'https://www.flickr.com/services/oauth/request_token'
urlAccessToken = 'https://www.flickr.com/services/oauth/access_token'
urlAuth = 'https://www.flickr.com/services/oauth/authorize'
cburl = "http://example.com"

authSess = requests_oauthlib.OAuth1Session(client_key=api_key, client_secret=api_secret, signature_method=u'HMAC-SHA1', signature_type=u'AUTH_HEADER', callback_uri=cburl)

request_token = authSess.fetch_request_token(urlRequestToken)
print(authSess.authorization_url(urlAuth))

redirect_response = input()
print(authSess.parse_authorization_response(redirect_response))
finalData=authSess.fetch_access_token(urlAccessToken)
print(finalData)
# {'fullname': 'Naman  Bansal', 'oauth_token': '72157719624682027-8697df180bd6c7e4', 'oauth_token_secret': 'bda3db94ceb2656b', 'user_nsid': '193572309@N03', 'username': 'namanewq'}
oauth_token=finalData['oauth_token']
oauth_token_secret=finalData['oauth_token_secret']
url="https://www.flickr.com/services/rest/?method=flickr.blogs.postPhoto&format=json"
auth=OAuth1(api_key,api_secret,oauth_token,oauth_token_secret)
params={'blog_id':'main-qimg-c4a52db497eb7f00c060f9b05559348c','photo_id':'1','title':'first blog','description':'first blog by api'}
a=requests.get(url,auth=auth,params=params)
print(a)
