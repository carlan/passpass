from flask import Flask, render_template, url_for, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET'])
def index():
    password = random.random()
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0')