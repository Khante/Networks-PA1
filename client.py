import http.client
import sys
import urllib
params = urllib.parse.urlencode({'x':sys.argv[3], 'y':sys.argv[4]})
conn = http.client.HTTPConnection(sys.argv[1], sys.argv[2])
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn.request("POST", "", params, headers) #added headers here
response = conn.getresponse()
print(response.status, response.reason)
conn.close()