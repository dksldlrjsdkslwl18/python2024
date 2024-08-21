import requests
serviceKey='PvwQu8EARiCchl8SCJJkx1g%2F2C5z55%2B2usx5wIYu1vZ1HzNZxNRuO2OzQlmK49PAdvNibw63yiuW7gzHWEVFUw%3D%3D'
url = 'http://apis.data.go.kr/3040000/noSmokingService/getNoSmkAreaList'
params ={'serviceKey' : serviceKey, 'type' : 'xml', 'numOfRows' : '10', 'pageNo' : '1', 'id' : '화양동-01-02-047' }

response = requests.get(url, params=params)
print(response.content)
