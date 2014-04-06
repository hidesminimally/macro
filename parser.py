
import urlparse
import urllib
import nutrition
from bs4 import BeautifulSoup
"""
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
"""

def create_food(url):
	try:
		htmltext = urllib.urlopen(url).read()
	except:
		print("Error!")
		print(url)
	soup = BeautifulSoup(htmltext)
	strings = []
	for text in soup.stripped_strings:
		strings.append(text)

	name = soup.find("form").get_text(strip=True)
	name.encode()


	fatn, fatp, carbn, carbp, protn, protp = 0, 0, 0, 0, 0, 0

	fat = []
	carb = []
	cholesterol = []
	sodium = []
	protein = []

	"""
	Parses for fat, carbs, protein
	"""
	for i in range(len(strings)):
		if strings[i] == "Total Fat":
			food = strings[i] + " " + strings[i + 1] + " " + strings[i+2] + strings[i+3]
			fat.append(food.encode('utf-8'))
			fatn = strings[i + 1]
			fatp = strings[i+2]
		if strings[i] == "Tot. Carb.":
			food = strings[i] + " " + strings[i + 1] + " " + strings[i+2] + strings[i+3]
			carb.append(food.encode('utf-8'))
			carbn = strings[i + 1]
			carbp = strings[i+2]
		if strings[i] == "Cholesterol":
			food = strings[i] + " " + strings[i + 1] + " " + strings[i+2] + strings[i+3]
			cholesterol.append(food.encode('utf-8'))
		if strings[i] == "Sodium":
			food = strings[i] + " " + strings[i + 1] + " " + strings[i+2] + strings[i+3]
			sodium.append(food.encode('utf-8'))
		if strings[i] == "Protein":
			food = strings[i] + " " + strings[i + 1]
			protein.append(food.encode('utf-8'))
			protn = strings[i + 1]


	"""
	parses for Calories
	"""
	gen = (line for line in soup.stripped_strings if "Calories" in line)

	calo = ""
	
	for line in gen:
		if not "Fat" in line:
			calo = line.strip()
			calo = ''.join([i for i in calo if i.isdigit()])
			#calo = int(calo)
		#else:
		#	fat = line.strip()
		#	fat = ''.join([i for i in calo if i.isdigit()])


	nut = nutrition.Food(name, fatn, fatp, carbn, carbp, protn, calo)
	#creates a Food object that contains floats denoting fat, carbs, etc.

	return nut
	
