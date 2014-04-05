import urlparse
import urllib
import parser
from bs4 import BeautifulSoup

url = "http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp"

urls = [url]
visited = [url]

while len(urls) > 0:
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print("Error")
		print(urls[0])
	soup = BeautifulSoup(htmltext)
	#print("Visited: " + urls[0])
	urls.pop(0)
	#print len(urls)


	for link in soup.find_all('a',href=True):
		#print(link['href'])
		link['href'] = urlparse.urljoin(url,link['href'])
		#print(link['href'])

		if "label.asp?" in link['href'] and link['href'] not in visited:
			urls.append(link['href'])
			visited.append(link['href'])
			parser.nutrition_parse(link['href'])
			#print link['href']




#yo
#print visited