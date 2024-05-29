from time import sleep
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from helium import *

driver = webdriver.Chrome()

baseUrl = "https://www.agoda.com"
searchKey = "/vi-vn/search?"

def get_town_link(districtLinkFile: str):
    districtFile = open(districtLinkFile, mode="r", encoding="utf-8")
    districtReader = csv.reader(districtFile)
    districtLink = list(districtReader)[1:]
    districtFile.close()
    
    towns = []
    for i in districtLink:
        driver.get(i[0])
        sleep(3)
        htmltext = driver.page_source
        soup = BeautifulSoup(htmltext, "html.parser")
        linkList = soup.findAll("script")
        linkList = str(linkList)
        index = linkList.find(searchKey)
        link = ""
        for j in range(index, index + 200):
            if linkList[j] == '"':
                break
            link = link + linkList[j]
        link = (baseUrl + link).replace('\\u0026', '&')
        towns.append(link)
        print("Done " + i[0] + ": " + str(link))
        sleep(3)
    return towns
