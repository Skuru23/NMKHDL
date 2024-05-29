from time import sleep
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from helium import *

driver = webdriver.Chrome()

def get_district_link(cityLinkFile: str):
    cityFile = open(cityLinkFile, mode="r", encoding="utf-8")
    cityReader = csv.reader(cityFile)
    cityLink = list(cityReader)[1:3]
    cityFile.close()

    districts = []
    for i in cityLink:
        driver.get(i[0])
        sleep(3)
        htmltext = driver.page_source
        soup = BeautifulSoup(htmltext, "html.parser")
        links = soup.find("section", class_="neighbor-class")
        try:
            link1 = links.findAll("a", href=True)
            for x in link1:
                if x.text:
                    link = "https://www.agoda.com" + x["href"]
                    districts.append(link)
            print("Done:  " + str(i))
        except:
            print("No thing: " + str(i))
            continue

    return districts
