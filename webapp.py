from flask import Flask, render_template, jsonify, url_for
import spider
import counter
import json

app = Flask(__name__)

@app.route('/')
def index():

	foods = spider.run()
	foodlist = foods[0]
	foodnames = []
	for food in foodlist:
		foodnames.append(food.get_name())
	count = counter.Counter()
	data = json.dumps(foodnames)







	#x = {'date':[u'2012-06-28', u'2012-06-29', u'2012-06-30'], 'users': [405, 368, 119]}

	return render_template('index.html', foodlist = foodlist, count = count, data = data )



if __name__ == '__main__':
    app.run(debug=True)