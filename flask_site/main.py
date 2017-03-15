#!/usr/bin/env python
from flask import Flask, render_template

# View site @ http://localhost:5000/

# Creating Flask App
app = Flask(__name__)

# Index Page
@app.route('/')
def index():
    return render_template('index.html')

# Setting app to run only if this file is run directly. 
if __name__ == '__main__':
    app.run(debug = True)