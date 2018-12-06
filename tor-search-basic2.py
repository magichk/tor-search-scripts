import requests
import collections

proxies = {'http': 'socks5h://127.0.0.1:9150',
			'https':'socks5h://127.0.0.1:9150'}

def getLinks(link):
        return[]

def crawl(directory):
    addresses = collections.deque()
    try:
        pagequeue = collections.deque()
        pagequeue.append(directory)
        while pagequeue:
            try:
                url=pagequeue.popleft()
                print(url)
                response=requests.get(url,proxies=proxies)
                if response.status_code == 200:
                    links = getLinks(response)
                    [pagequeue.append(link) for link in links]

            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

    except requests.exceptions.Timeout:
        pass
    except requests.exceptions.TooManyRedirects:
        pass
    except requests.exceptions.RequestException as e:
        pass
    except:
        import sys, traceback
        traceback.print_exc(file=sys.stdout)

def searchUnderDir(address):
    for page in range(1,4):
        for searchItem in ['element1', 'element2', 'element3']:
            addressWithCriteria = address.replace('CRITERIA_WILDCARD', searchItem)
            addressToSearch = addressWithCriteria+str(page)
            crawl(addressToSearch)

searchUnderDir('http://underdj5ziov3ic7.onion/search/CRITERIA_WILDCARD/pg')
