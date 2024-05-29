from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from helium import *
driver = webdriver.Chrome()

def get_city_link(webLink: str):
    print(webLink)
    driver.get(webLink)
    sleep(3)
    htmltext = driver.page_source
    soup = BeautifulSoup(htmltext, "html.parser")
    cityLinks = []
    links=soup.find("section",class_="all-states-class")
    link1 = links.findAll("a",href=True)
    for x in link1:
        if x.text:
            link="https://www.agoda.com"+x['href']
            cityLinks.append(link)
    return cityLinks