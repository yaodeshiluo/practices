from flask import Flask
from flask import render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db':'todo'}
db = MongoEngine(app)

@app.route('/')
def index():
    return render_template('index.html')