import os
import requests
import shutil

from download_util import download_file

BASE_DIR = os.path.dirname(os.path.join(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOAD_DIR, "1.jpg")

url = "https://i.natgeofe.com/n/3f2a2e55-47f9-4dda-9f03-bbbd4e9d343e/Trav%20Lake%20GettyImages-909708218_4x3.jpg"

r = requests.get(url, stream=True)
r.raise_for_status()
with open(downloaded_img_path, "wb") as f:
    f.write(r.content)

download_file(url, DOWNLOAD_DIR)
