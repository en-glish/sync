import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
f = open('afarinish_dl_links.txt','a+')

for category in [482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 278, 531]:
    for page in range(1, 200):          
        url = "https://www.afarinesh.org/?wpdmtask=get_downloads&pg=3692&category={category}&cp={page}".format(page=page,category=category)        
        status, response = http.request(url)
        soup = BeautifulSoup(response, parse_only=SoupStrainer('a'), features='lxml')
        print (len(soup))
        if len(soup)==0:
            break;
        for link in soup:
            if link.has_attr('onclick'):
                url = link['onclick']
                f.writelines(url[15:url.find(';')-1] + '\n')
                f.flush()
f.close()
