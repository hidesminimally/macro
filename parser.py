import urlparse
import urllib
from bs4 import BeautifulSoup

def nutrition_parse(url):
	try:
		htmltext = urllib.urlopen(url).read()
	except:
		print("Error!")
		print(url)
	soup = BeautifulSoup(htmltext)

	print(soup)
