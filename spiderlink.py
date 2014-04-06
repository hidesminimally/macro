import urlparse
import urllib
import parser
from bs4 import BeautifulSoup


class Nutrition:
	def __init__ (self):

		self.calorie_text = []
		self.nutrition = {}

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
					information = parser.nutrition_parse(link['href'])
					self.calorie_text.append(information[0])
					self.nutrition[information[0]] = (information[1],information[2])

					#parser.nutrition_parse currently parses the calories

	def get_food(self):
		return self.calorie_text

	def get_food_string(self):
		return str('\n'.join(self.calorie_text))

	def get_calorie_from_food(self,food):
		return self.nutrition[food][1]

	def get_fatcalorie_from_food(self,food):
		return self.nutrition[food][2]





#print visited