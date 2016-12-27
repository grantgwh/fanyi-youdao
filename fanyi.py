import urllib.parse
import urllib.request
import json
import time

keyword=input('please input text:')
url =\
 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
data={}

data['action']='FY_BY_CLICKBUTTON'
data['doctype']='json'
data['i']=keyword
data['keyfrom']='fanyi.web'
data['type']='AUTO'
data['typoResult']='true'
data['ue']='UTF-8'
data['xmlVersion']='1.8'
data = urllib.parse.urlencode(data).encode('utf-8')


req = urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')
target=json.loads(html)
target=target['translateResult'][0][0]['tgt']

time.sleep(2)
print(target)
