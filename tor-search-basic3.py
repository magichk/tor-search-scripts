import requests
import collections

proxies = {'http': 'socks5h://127.0.0.1:9150',
			'https':'socks5h://127.0.0.1:9150'}

def __isValidAddress(link):
    from validators.url import url
    from validators.length import length
#    import validators
    plainLink = link["href"].replace(".tor2web.org", ".onion")

    if "http://" not in plainLink and "https://" not in plainLink:
        plainLink = "http://"+plainLink

    if ".onion" in plainLink and url(plainLink):
        plainLink = plainLink[0:plainLink.find(".onion")]
        if length(plainLink, min=16) or length(plainLink, min=56):
            return plainLink + ".onion" 
        else:
            return none
    else:
        if url(plainLink):
            return plainLink
        else:
            return None

def getLinks(response):
    from bs4 import BeautifulSoup 
    soup = BeautifulSoup(response.text, "lxml")
    links = soup.find_all('a', attrs = {"href" : True})
    addresses = set()
    for link in links:
        address = __isValidAddress(link)
        if address is not None:
            addresses.add(address)
    return addresses


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
