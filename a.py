from time import sleep
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from helium import *

driver = webdriver.Chrome()

baseUrl = "https://www.agoda.com"
searchKey = "/vi-vn/search?"

def get_district_link(cityLinkFile: str):
    cityFile = open(cityLinkFile, mode="r", encoding="utf-8")
    cityReader = csv.reader(cityFile)
    cityLink = list(cityReader)[2:3]
    cityFile.close()

    districts = []
    for i in cityLink:
        print(i[0])
        driver.get(i[0])
        htmltext = driver.page_source
        soup = BeautifulSoup(htmltext, "html.parser")
        links = soup.find("section", class_="neighbor-class")
        try:
            link1 = links.findAll("a", href=True)
            for x in link1:
                if x.text:
                    link = "https://www.agoda.com" + x["href"]
                    
                    driver.get(link)
                    sleep(3)
                    htmltext = driver.page_source
                    soup = BeautifulSoup(htmltext, "html.parser")
                    linkList = soup.findAll("script")
                    linkList = str(linkList)
                    text_file = open("Output.txt", "w", encoding="utf-8")
                    text_file.write(linkList)
                    text_file.close()
                    index = linkList.find(searchKey)
                    link = ""
                    for j in range(index, index + 150):
                        if linkList[j] == '"':
                            break
                        link = link + linkList[j]
                    link = (baseUrl + link).replace('\\u0026', '&')
                    districts.append(link)
                    print("Done:  " + link)
        except:
            print("No thing: " + i[0])
            continue
        print(link) 
        
       
        
    return districts
get_district_link("./Data/city.csv")
