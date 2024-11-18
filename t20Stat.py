import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


page_url = 'https://www.iplt20.com/stats/2023'
#print(page_url)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#driver = webdriver.Chrome(options=chrome_options)
driver.get(page_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.close()

table = soup.find('table')
headers = [header.text.strip() for header in table.find_all('th')]
#print(headers)
rows = table.find_all('tr')
#print(rows)

data = []
for row in rows[1:]:
    cells = row.find_all('td')
    data.append([cell.text.strip() for cell in cells])

#print(data)
df = pd.DataFrame(data, columns = headers)
#print(df)
st.table(df)


