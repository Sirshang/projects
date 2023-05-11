import requests

base_url = 'http://www.httpbin.org/'
data = {
    "user": "123"
}
r = requests.get(base_url+'get', params=data)
print(r.url)
print(r.status_code)

r = requests.post(base_url+'post', data=data)
print(r.url)
print(r.text)