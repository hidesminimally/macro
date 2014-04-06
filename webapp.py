from flask import Flask
import spider
app = Flask(__name__)

@app.route('/')
def index():
	foodlist = spider.run()
	return render_template('index.html', foodlist = foodlist)

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)