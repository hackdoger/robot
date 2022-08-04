import http.client, urllib
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'你的APIKEY','question':'robot'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/robot/index',params,headers)
res = conn.getresponse()
data = res.read()
print(data.decode('utf-8'))
