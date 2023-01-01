from fastapi import FastAPI
from scrape import run as scrape_runner

app = FastAPI()

@app.get("/")
# http://localhost:8000/
def hello_world():
    # you can run other code here
    return {"hello": "world"}

# http://localhost:8000/box-office-scraper
@app.post("/box-office-scraper")
def box_office_scraper_view():
    # you can run other code here
    scrape_runner()
    return {"done": [1,2,3]}
