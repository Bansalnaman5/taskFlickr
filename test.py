import requests
url='https://www.flickr.com/services/rest/?method=flickr.photos.getPopular'
params={'api_key':'b77b2fc41549f6dee570f482b5e2dd77','user_id':'193572309@N03'}
a=requests.get(url,params=params)
print(a)
print(a.text)
