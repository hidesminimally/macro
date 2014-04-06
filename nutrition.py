
import urlparse
import urllib
from bs4 import BeautifulSoup

class Food:
	def __init__(self, name, fat, fatp, carb, carbp, protein, calorie):
		self.name = str(name)
		self.fat = convertToFloat(fat)
		self.fatp = convertToFloat2(fatp)
		self.carb = convertToFloat(carb)
		self.carbp = convertToFloat2(carbp)
		self.protein = convertToFloat(protein)
		self.calorie = convertToFloat2(calorie)





	def __repr__(self):
		try:
			return self.name + " | Fat:" + str(self.fat) + "g | Carbs:" + str(self.carb) + "g | Protein:" + str(self.protein) +"g | Calories:" + str(self.calorie)
		except:
			print("UNICODE ERROR")
			return "error"

	def get_name(self):
		return self.name
	def get_fat(self):
		return self.fat
	def get_carbs(self):
		return self.carb
	def get_protein(self):
		return self.protein
	def get_calorie(self):
		return self.calorie













"""
==============================================
Extra functions used to parse strings into floats
=============================================

"""

def convertToFloat(obj):
		try:
			obj= float(obj[:len(obj)-1])
		except:
			return None
		return obj

def convertToFloat2(obj):
	try:
		obj = float(obj)
	except:
		return None

	return obj
