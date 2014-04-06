
class Counter:
	def __init__(self):
		self.fat = 0
		self.fatp = 0
		self.carb = 0
		self.carbp = 0
		self.protein = 0
		self.calorie = 0





	def __repr__(self):
		try:
			return  " | Fat:" + str(self.fat) + "g | Carbs:" + str(self.carb) + "g | Protein:" + str(self.protein) +"g | Calories:" + str(self.calorie)
		except:
			print("UNICODE ERROR")
			return "error"

	def get_fat(self):
		return self.fat
	def get_carbs(self):
		return self.carb
	def get_protein(self):
		return self.protein
	def get_calorie(self):
		return self.calorie