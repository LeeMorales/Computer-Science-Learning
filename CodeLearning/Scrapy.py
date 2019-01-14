import urllib
from webscraping import xpath,common
def get_data(url):
    req = urllib.request.urlopen(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')
    reponse = urllib.request.urlopen(req)
    html = reponse.read()
    title = xpath.search(html, '//div[@class="av style1"]/a[1]/@title')
    return title
f=open(r'D:\f.txt','w')
for p in range(1,494):
    url = r'http://dmm18.net/index.php?pageno_b=%s'%p
    print (url)
    title = get_data(url)
    for  item1 in title:            
            f.write(str(item1)+'\n')
            print (item1)
f.close()