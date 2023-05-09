from flask import Flask

app = Flask (_name_)

@app.route('/')
def home():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'About'
