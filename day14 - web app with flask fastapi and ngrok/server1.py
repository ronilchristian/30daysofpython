from flask import Flask
from scrape import run as scrape_runner

app = Flask(__name__)

# http://localhost:8000/
@app.route("/", methods=['GET'])
def hello_world():
    # you can run other code here
    return "Hello World! This is Flask"

# http://localhost:8000/box-office-scraper
@app.route("/box-office-scraper", methods=['POST'])
def box_office_scraper_view():
    # you can run other code here
    scrape_runner()
    return {"done": [1,2,3]}
