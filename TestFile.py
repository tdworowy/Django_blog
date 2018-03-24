import requests
try:
    print(requests.get("http://localhost:8083/blog").text)
except Exception as ex:
    print(ex)
    print(print(requests.get("http://localhost:8083").text))