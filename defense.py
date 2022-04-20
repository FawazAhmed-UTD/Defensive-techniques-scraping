import json

from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# launch url
attacks = []
url = "https://d3fend.mitre.org/"
main_counter = 0
total_defensive_technique = 0
max = -1000
min = 1000
avg = 0
count_of_zero = 0
# create a new Firefox session
driver = webdriver.Firefox(executable_path='geckodriver.exe')
# driver.implicitly_wait(30)
driver.get(url)

# After opening the url above, Selenium clicks the specific link
driver.find_element_by_class_name('svelte-1m22did').click()

# Selenium hands the page source to Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

# textfile = open("defensive_technique_info.txt", "w")
# textfile.write("Defensive Technique Name\t\t" + "Techniques/Sub-Techniques it is a solution to" + "\n")
# '''for element in names:
#     textfile.write(element + "\n")
# textfile.close()'''

for a in soup.find_all('a', href=True):
    link = a['href']
    if ("technique" in link):  # for each defensive technique
        count = 0
        link = url + link
        print(link)
        # defensive_technique_data = requests.get(link)
        driver.get(link)
        vSoup = BeautifulSoup(driver.page_source, 'lxml')
        title = vSoup.find('h1', {"class": "svelte-1rpoqsw"})
        if (title != None):
            headers = ['']
            bodys = []
            title = title.text
            info = vSoup.find('div', {"class": "text-justify"}).contents
            definition = ''
            toSave = {'Definition': info.pop(0).text}
            currentHeader = ''

            for x in info:
                y = str(x)
                if '<h2' in y:
                    currentHeader = x.text
                    toSave[currentHeader] = ''
                elif currentHeader == '':
                    toSave['Definition'] += (' ' + x.text)
                elif '<p' in y or '<li' in y:
                    toSave[currentHeader] += (' ' + x.text)

            toSave = {title: toSave}
            attacks.append(toSave)

with open('defensive_technique_info.json', 'w') as file:
    json.dump(attacks, file)
