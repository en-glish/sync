import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()

for key, value in {'630':'exam', '158':'speaking','157':'reading', '156':'listening', '160':'vocabulary', '161':'books', '744':'multi_purpose_books', '159':'grammer'}.items():
    f = open('afarinish_'+value+'_links.txt','a+')
    for page in range(1, 200):          
        url = "https://www.afarinesh.org/?wpdmtask=get_downloads&pg=519&category={category}&cp={page}".format(page=page,category=key)        
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
