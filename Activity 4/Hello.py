from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/act1')
def act1():
    return render_template('act1.html')

@app.route('/act2')
def act2():
    return render_template('act2.html')

@app.route('/act3')
def act3():
    return render_template('act3.html')

app.run(host="localhost", debug=True)