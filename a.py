from time import sleep
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from helium import *
import pandas as pd

driver = webdriver.Chrome()
linkTown = [
    "https://www.agoda.com/vi-vn/city/ho-chi-minh-city-vn.html?cid=1844104",
]


def strs(x):
    return str(x)


def getPagelist():
    authors = []
    for i in linkTown:
        driver.get(i)
        sleep(3)
        htmltext = driver.page_source
        soup = BeautifulSoup(htmltext, "html.parser")
        list = soup.findAll("script")
        list = strs(list)
        text_file = open("Output.txt", "w", encoding="utf-8")
        text_file.write(list)
        text_file.close()
        url1 = "/vi-vn/search?"
        index = list.find(url1)
        link = ""
        for j in range(index, index + 200):
            if list[j] == '"':
                break
            else:
                print(link)
                link = link + list[j]
        authors.append(link)
        print("xong cua " + i + " la: " + strs(link))
        sleep(3)
    return authors


link = getPagelist()
print(link)
