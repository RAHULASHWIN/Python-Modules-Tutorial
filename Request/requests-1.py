import requests

payload = {"firstName": "john", "lastName":"Smith"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
