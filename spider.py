import urlparse
import urllib
import parser
from bs4 import BeautifulSoup

calorie_text = []
nutrition = {}
url = "http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp"
urls = [url]
visited = [url]

while len(urls) > 0:
	try:
		htmltext = urllib.urlopen(urls[0]).read()
				#Opens the url
	except:
		print("Error")
		print(urls[0])
	soup = BeautifulSoup(htmltext)
	urls.pop(0)



	for link in soup.find_all('a',href=True):
		link['href'] = urlparse.urljoin(url,link['href'])

		if "label.asp?" in link['href'] and link['href'] not in visited:
					#opens the link for different foods
					#urls.append(link['href'])
					#visited.append(link['href'])
			#information = parser.nutrition_parse(link['href'])
			print parser.test(link['href'])
			#calorie_text.append(information[0])
			#nutrition[information[0]] = (information[1],information[2])

					#parser.nutrition_parse currently parses the calories

print nutrition