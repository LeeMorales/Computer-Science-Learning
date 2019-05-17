import urllib
response = urllib.request.urlopen("http://www.zhihu.com")
print (response.read())
