import requests
serviceKey='PvwQu8EARiCchl8SCJJkx1g%2F2C5z55%2B2usx5wIYu1vZ1HzNZxNRuO2OzQlmK49PAdvNibw63yiuW7gzHWEVFUw%3D%3D'

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
air=response.text
print(type(air))