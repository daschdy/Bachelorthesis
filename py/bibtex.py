import os
import requests

from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.realpath(__file__))
dotenv_path = os.path.join(script_dir, ".env")
load_dotenv(dotenv_path)
USER_ID = os.getenv("USER_ID")
API_KEY = os.getenv("API_KEY")
EXPORT_FORMAT = os.getenv("EXPORT_FORMAT")

url = f"https://api.zotero.org/users/{USER_ID}/items/top?format={EXPORT_FORMAT}"
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    file_name = "exported_references.bib"
    with open(file_name, "w", encoding='utf-8') as f:
        f.write(response.text)
    print("Export successful! File saved as exported_references.bib")
else:
    print("Error:", response.status_code, response.text)
