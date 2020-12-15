import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json

url = "https://gol.gg/champion/list/season-ALL/split-ALL/tournament-EU%20Masters%20Spring%20Play-In%202020/"

option = Options()
option.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install())


def getData(i):

    league = driver.find_element_by_xpath(
        '//*[@id="cbtournament"]/option[{0}]'.format(i))
    leagueName = league.get_attribute('value')
    league.click()

    time.sleep(5)

    element = driver.find_element_by_class_name('table_list')

    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    df = pd.read_html(str(table))[0]
    df = df.fillna(0)
    tableDict = {}
    tableDict = df.to_dict('records')

    js = json.dumps(tableDict)
    fp = open('{0}.json'.format(leagueName), 'w')
    fp.write(js)
    fp.close()


driver.get(url)

getData(8)
getData(105)
getData(194)
getData(279)
getData(333)
getData(370)
getData(405)
getData(416)

driver.quit()
