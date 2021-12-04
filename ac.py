from selenium import webdriver
from pyvirtualdisplay import Display
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from datetime import date
import json
pd.set_option('display.max_rows', None)

f = open("./BAU.json",)
data = json.load(f)

#write_to_file(_date, datas)
def write_to_file(_date, flights):
    filename = '/tmp/acstatus-{}.csv'.format(_date)

    with open(filename, 'a') as f:
        for i in data["bau"]:
            for j in datas:
                if(j == i):
                    f.write(f"{j} : {datas[j]} \n")
    return

_date = f"{date.today()}"

driver = webdriver.Chrome(executable_path="~/Desktop/CODE/ac_sync/chromedriver")

driver.get("Grafana Link")
print("Login page is opened")
driver.maximize_window()

username = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input")
password = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/div[2]/div/div/form/div[2]/div[2]/div/div/input")

username.send_keys("E-Mail")
password.send_keys("Password")

driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/div[2]/div/div/form/button").click()
time.sleep(3)

driver.get("Grafana Link 1")
time.sleep(15)
content = driver.page_source
soup = BeautifulSoup(content)
titles = []
values = []
datas = {}
list1 = soup.findAll('span', attrs={'class':'panel-title-text'})
for i in list1:
    titles.append(f"{i.text}")
list2 = soup.findAll('div', attrs={'class':'panel-content panel-content--no-padding'})
for j in list2:
    values.append(f'{j.div.div.div.div.div.div.contents[0].text}')
for k in range(0, len(list1)):
    v = None
    for i in data["bau"]:
        if (titles[k] == i):
            v = True
        if (v == True):
            break
    if(v == None):
        continue
    if(values[k] == "No data"):
        datas.update({f"{titles[k]}" : f"No data - Check"})
    elif(values[k].split(" ")[0] == "?"):
        datas.update({f"{titles[k]}" : f"Red - Check"})
    elif(values[k] == "✔"):
        datas.update({f"{titles[k]}" : f"Green - OK"})
    elif(values[k] == "🛠"):
        datas.update({f"{titles[k]}" : f"Maintenance - Check"})
    else:
        datas.update({f"{titles[k]}" : f"{values[k]} - OK"})
print("---------")
driver.get("Grafana Link 2")
time.sleep(15)
content = driver.page_source
soup = BeautifulSoup(content)
titles = []
values = []
list1 = soup.findAll('span', attrs={'class':'panel-title-text'})
for i in list1:
    titles.append(f"{i.text}")
list2 = soup.findAll('div', attrs={'class':'panel-content panel-content--no-padding'})
for j in list2:
    values.append(f'{j.div.div.div.div.div.div.contents[0].text}')
for k in range(0, len(list1)):
    v = None
    for i in data["bau"]:
        if (titles[k] == i):
            v = True
        if (v == True):
            break
    if(v == None):
        continue
    if(values[k] == "No data"):
        datas.update({f"{titles[k]}" : f"No data - Check"})
    elif(values[k].split(" ")[0] == "?"):
        datas.update({f"{titles[k]}" : f"Red - Check"})
    elif(values[k] == "✔"):
        datas.update({f"{titles[k]}" : f"Green - OK"})
    elif(values[k] == "🛠"):
        datas.update({f"{titles[k]}" : f"Maintenance - Check"})
    else:
        datas.update({f"{titles[k]}" : f"{values[k]} - OK"})
print("---------")
driver.get("Grafana Link 3")
time.sleep(15)
content = driver.page_source
soup = BeautifulSoup(content)
titles = []
values = []
list1 = soup.findAll('span', attrs={'class':'panel-title-text'})
for i in list1:
    titles.append(f"{i.text}")
list2 = soup.findAll('div', attrs={'class':'panel-content panel-content--no-padding'})
for j in list2:
    values.append(f'{j.div.div.div.div.div.div.contents[0].text}')
for k in range(0, len(list1)):
    v = None
    for i in data["bau"]:
        if (titles[k] == i):
            v = True
        if (v == True):
            break
    if(v == None):
        continue
    if(values[k] == "No data"):
        datas.update({f"{titles[k]}" : f"No data - Check"})
    elif(values[k].split(" ")[0] == "?"):
        datas.update({f"{titles[k]}" : f"Red - Check"})
    elif(values[k] == "✔"):
        datas.update({f"{titles[k]}" : f"Green - OK"})
    elif(values[k] == "🛠"):
        datas.update({f"{titles[k]}" : f"Maintenance - Check"})
    else:
        datas.update({f"{titles[k]}" : f"{values[k]} - OK"})
write_to_file(_date, datas)
driver.close()
