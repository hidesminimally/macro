
import urlparse
import urllib
from bs4 import BeautifulSoup

def nutrition_parse(url):
	calorie = ""
	try:
		htmltext = urllib.urlopen(url).read()
	except:
		print("Error!")
		print(url)
	soup = BeautifulSoup(htmltext)

	food = soup.find("form").get_text(strip=True)
	food.encode()
	
	gen = (line for line in soup.stripped_strings if "Calories" in line)
	
	for line in gen:
		if not "Fat" in line:
			calo = line.strip()
			calo = ''.join([i for i in calo if i.isdigit()])
			#calo = int(calo)
		else:
			fat = line.strip()
			fat = ''.join([i for i in calo if i.isdigit()])
	calorie = food + ' ' + "Calories: " + calo + ", Calories from Fat: " + fat

			#print(calo)
	return (calorie, int(calo), int(fat))

def test(url):
	try:
		htmltext = urllib.urlopen(url).read()
	except:
		print("Error!")
		print(url)
	soup = BeautifulSoup(htmltext)

	food = soup.find("font size ='3'").get_text(strip=True)
	print food