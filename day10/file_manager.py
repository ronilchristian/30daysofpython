import os

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJ_DIR = os.path.dirname(BASE_DIR)

email_txt = os.path.join("templates", "email.txt")

content = ""

with open(email_txt, "r") as file:
    content = file.read()

print(content.format(name="Ronil"))