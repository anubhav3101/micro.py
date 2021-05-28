from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/home')
def mine():
    return 'My nanme is ujjawal'  #use / and then home to see this string

app.run(host='0.0.0.0', port=9000)
