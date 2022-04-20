import json
import requests
from bs4 import BeautifulSoup

URL = "https://attack.mitre.org/matrices/enterprise/"
page = requests.get(URL)
names = []

technique_URL = "https://attack.mitre.org"

soup = BeautifulSoup(page.content, "html.parser")
for l in soup.find_all(['a']):
    link = str(l.get('href'))
    link = technique_URL + link
    # print(link)
    if(("techniques" in link) and ("T" in link)):
        page = requests.get(link)
        getter = BeautifulSoup(page.content, "html.parser")
        title = getter.find('h1')
        description = getter.find_all("div", {"class": "description-body"})[0].text

        if(title!=None):
            if(':' in title.text):
                print(str((title.text).split(":")[1]).strip())
                names.append({str((title.text).split(":")[1]).strip(): description})
            else:
                print(str(title.text).strip())
                names.append({str(title.text).strip(): description})

with open("techniques_and_sub_techniques_names.json", "w") as file:
    json.dump(names, file)
