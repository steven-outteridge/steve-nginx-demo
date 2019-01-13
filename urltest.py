#!/usr/local/bin/python
import sys
import httplib
from urlparse import urlparse
urlin = raw_input("url=")
print urlin

def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400

if __name__ == '__main__':
 #   testUrl = checkUrl('http://192.168.0.233:8080') # URL is up
    testUrl = checkUrl('http://'+urlin) # Test
    if [ testUrl == "True"]:
       print "Steves URL is up"
