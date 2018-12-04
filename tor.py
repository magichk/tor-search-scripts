import requests
proxies = {'http': 'socks5h://127.0.0.1:9150',
			'https':'socks5h://127.0.0.1:9150'}

def searcherUnderDir(address):
	for page in range(1,4):
		for searchItem in ['term1', 'term2']:
			addressWithCriteria = address.replace("CRITERIA_WILDCARD", searchItem)
			addressToSearch=addressWithCriteria+str(page)
			print(addressToSearch)
			response = requests.get(addressToSearch, proxies=proxies)
			print(response)

searcherUnderDir('http://underdj5ziov3ic7.onion/search/CRITERIA_WILDCARD/pg/')
