# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:03:02 2023

@author: abhis
"""

import pandas as pd
import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import json
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
import csv
import os

df = pd.read_csv('ticker_names.csv')

# Ensure the directory for storing the HTML files exists
output_directory = 'saved_transcripts'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
#options.add_argument("--no-sandbox")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

left_ones=[]

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    ticker = row['ticker_hist']
    url = f"https://strike.market/stocks/{ticker}/earnings-call-transcripts"  # Replace with the actual URL structure you want to use
    driver.get(url)
    if ('Strike.Market – Stock Forecast, Predictions & Alternative data' in driver.title):
        left_ones.append(ticker)
    else:
        element_name = str(row['Quarter']) + ' ' + str(row['Year']) + ' Earnings Call Transcript'
        try:
            anchor_element = driver.find_element(By.LINK_TEXT, element_name)
            link = anchor_element.get_attribute('href')
            driver.get(link)
            page_source = driver.page_source
            with open(os.path.join(output_directory, f"{ticker}_{row['Quarter']}_{row['Year']}.html"), 'w', encoding='utf-8') as file:
                file.write(page_source)    
        except Exception as e:
            left_ones.append(ticker)

print(left_ones)
driver.quit()