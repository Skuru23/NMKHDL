from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helium import *
import csv

driver = webdriver.Chrome()

def get_hotel_links(districtLinkFile: str):
    districtFile = open(districtLinkFile, mode="r", encoding="utf-8")
    districtReader = csv.reader(districtFile)
    districtLinkLink = list(districtReader)[1:2]
    districtFile.close()
    
    hotels = []
    for i in districtLinkLink:
        print("Current district: " + i[0])
        a = 0
        page = 1
        driver.get(i[0])
        sleep(5)
        while a == 0:
            print("currentpage: " + str(page))
            sleep(2)
            lastHeight = driver.execute_script("return document.body.scrollHeight")
            while True:
                jumpToThisHeight = lastHeight * 2 / 3 # Tùy chỉnh theo màn hình
                driver.execute_script(f"window.scrollTo(0, {jumpToThisHeight});")
                sleep(5) 
                newHeight = driver.execute_script("return document.body.scrollHeight")
                if newHeight == lastHeight:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(5)
                    finalHeight = driver.execute_script("return document.body.scrollHeight")
                    if finalHeight == newHeight:
                        break 

                lastHeight = newHeight
            sleep(5)
            htmltext = driver.page_source
            soup = BeautifulSoup(htmltext, "html.parser")
            links = soup.findAll("a", class_="PropertyCard__Link")
            text_file = open("Output.txt", "w", encoding="utf-8")
            text_file.write(str(links))
            text_file.close()
            for x in links:
                try:
                    link = "https://www.agoda.com" + x["href"]
                    hotels.append(link)
                    print(link)
                except:
                    print("No link")
            print("Có tát cả " + str(len(links)) + " khách sạn")
            try:
                # Wait until the button is clickable
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "paginationNext"))
                )
                next_button.click()
                print("Successfully clicked the 'Next Page' button.")
                page = page + 1
            except Exception as e:
                print(f"Failed to find or click the button: {e}")
                a = 1
        sleep(2)
    return hotels
