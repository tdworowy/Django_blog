import requests
import sys

if len(sys.argv) < 2:
    ip = 'localhost'
else:
    ip = sys.argv[1]

try:
    print(requests.get("http://%s:8083/blog/" % ip).text)
except Exception as ex:
    print(ex)
    print(requests.get("http://%s:8083" % ip).text)
