from flask import Flask, render_template
import spider
import counter 

app = Flask(__name__)

@app.route('/')
def index():
	fooddict = {}
	foods = spider.run()
	foodlist = foods[0]
	dictionary = foods[1]
	fat_contents = []
	food_names = []
	for food in foodlist:
		fat_contents.append(food.get_fat())
		food_names.append(food.get_name())
	fooddict['food'] = food_names
	fooddict['fat'] = fat_contents
	count = counter.Counter()




	#x = {'date':[u'2012-06-28', u'2012-06-29', u'2012-06-30'], 'users': [405, 368, 119]}

	return render_template('index.html', foodlist = foodlist, count = count)



if __name__ == '__main__':
    app.run(debug=True)