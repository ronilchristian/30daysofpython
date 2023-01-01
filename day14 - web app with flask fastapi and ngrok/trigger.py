import requests

ngrok_url = "https://ba6b-73-246-53-192.ngrok.io"
endpoint = f"{ngrok_url}/box-office-scraper"

r = requests.post(endpoint, json={})
print(r.json())