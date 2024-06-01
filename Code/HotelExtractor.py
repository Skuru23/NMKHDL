import pandas as pd
from time import sleep
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from helium import *
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree

driver = webdriver.Chrome()

# Link khách sạn,Độ sạch sẽ,Sự thoải mái và chất lượng phòng,Dịch vụ,Vị trí,Tiện nghi,Số lượng phòng,Số lượng nhà hàng,Số quán bar,Thang máy,Tiêu chuẩn về an toàn,Bể bơi, Bồn tắm, Ghế Sofa,Phòng xông hơi, Spa, Mát-xa,Phòng tập,Sân golf, Sân quần vợt, Rate Star

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, "a+", newline="") as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(list_of_elem)


def getInfor(link):
    dict = {
        "Link khách sạn": "nan",
        "Độ sạch sẽ": "nan",
        "Sự thoải mái và chất lượng phòng": "nan",
        "Dịch vụ": "nan",
        "Vị trí": "nan",
        "Tiện nghi": "nan",
        "Số lượng phòng": "nan",
        "Số lượng nhà hàng": "nan",
        "Số quán bar": "nan",
        "Thang máy": "nan",
        "Tiêu chuẩn về an toàn": "nan",
        "Bể bơi": "nan",
        "Bồn tắm": "nan",
        "Ghế Sofa": "nan",
        "Phòng xông hơi": "nan",
        "Spa": "nan",
        "Mát-xa": "nan",
        "Phòng tập": "nan",
        "Sân golf": "nan",
        "Sân quần vợt": "nan",
        "Rate Star": "nan",
    }
    driver.get(link)
    sleep(5)
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        jumpToThisHeight = lastHeight / 2 # Tùy chỉnh theo màn hình
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
    WebDriverWait(driver, 5)
    htmltext = driver.page_source
    soup = BeautifulSoup(htmltext, "html.parser")

    dom = etree.HTML(str(soup))
    
    room1 = NULL
    room = dom.xpath("//span[text()='Số lượng phòng']")
    if room:
        room1 = room[0].xpath("following-sibling::span[1]")
        if room1:
            room1 = room1[0].text
            print("Room:", room1)
    
    restaurant = dom.xpath("//span[text()='Số lượng nhà hàng']")
    
    restaurant1 = NULL
    if restaurant:
        restaurant1 = restaurant[0].xpath("following-sibling::span[1]")
        if restaurant1:
            restaurant1 = restaurant1[0].text
            print("Restaurant:", restaurant1)
     
    bar1 = NULL       
    bar = dom.xpath("//span[text()='Số lượng nhà hàng']")
    if bar:
        bar1 = bar[0].xpath("following-sibling::span[1]")
        if bar1:
            bar1 = bar1[0].text
            print("Bar:", bar1)

    # # Lấy phòng

    # Lấy tất cả phần đánh giá
    point = soup.find("div", class_="Review-travelerGrade-Cell")

    # Lấy thang máy
    thangMay = dom.xpath("//span[contains(text(), 'Thang máy')]")

    # Tiêu chuẩn về an toàn
    anToan = dom.xpath("//span[contains(text(), 'an toàn')]")

    # Thư giãn và vui chơi giải trí
    beBoi  = dom.xpath("//span[contains(text(), 'Bể bơi')]")
    xong = dom.xpath("//span[contains(text(), 'Xông')]")
    
    matXa = dom.xpath("//span[contains(text(), 'Mát-xa')]")
    sanGolf = dom.xpath("//span[contains(text(), 'Sân gôn')]")
    sanQuanVot = dom.xpath("//p[contains(text(), 'Tennis')]")
    sPa = dom.xpath("//span[contains(text(), 'Spa')]")
    phongTap = dom.xpath("//span[contains(text(), 'Phòng tập')]")

    # Trang bị trong phòng
    bonTam = dom.xpath("//span[contains(text(), 'Bồn tắm')]") 
    gheSofa = dom.xpath("//span[contains(text(), 'Ghế sofa')]") 

    # Số sao
    star = soup.findAll("svg", class_="bHHfTR")
    
    dict["Link khách sạn"] = link
    try:
        point1 = point.findAll("span")
        if len(point1) > 0:
            i = 0
            while i < len(point1):
                if point1[i].text in dict:
                    dict[point1[i].text] = point1[i + 1].text
                    i = i + 2
                else:
                    i = i + 2
    except:
        print("Không có phần đánh giá")
    if room1:
        try:
            dict["Số lượng phòng"] = (int)(room1)
        except:
            pass
        
    if restaurant1:
        try:
            dict["Số lượng nhà hàng"] = (int)(restaurant1)
        except:
            pass

    if bar1:
        try:
            dict["Số quán bar"] = (int)(bar1)
        except:
            pass

    # Điền vào thang máy
    if len(thangMay) > 0:
        for i in thangMay:
            if i.text == "Thang máy":
                dict["Thang máy"] = 1

    # Điền vào tiêu chuẩn về an toàn
    if len(anToan) == 1:
        dict["Tiêu chuẩn về an toàn"] = 1

    # Điền vào thư giãn vui chơi giải trí

    if len(beBoi) > 0:
        dict["Bể bơi"] = 1
    if len(beBoi) == 0 :
        dict["Bể bơi"] = 0

    if len(xong) > 0:
        dict["Phòng xông hơi"] = 1
    if len(xong) == 0:
        dict["Phòng xông hơi"] = 0

    if len(matXa) > 0:
        dict["Mát-xa"] = 1
    if len(matXa) == 0:
        dict["Mát-xa"] = 0

    if len(sanGolf) > 0:
        dict["Sân golf"] = 1
    if len(sanGolf) == 0:
        dict["Sân golf"] = 0

    if len(sanQuanVot) > 0:
        dict["Sân quần vợt"] = 1
    if len(sanQuanVot) == 0:
        dict["Sân quần vợt"] = 0

    if len(sPa) > 0:
        dict["Spa"] = 1
    if len(sPa) == 0:
        dict["Spa"] = 0

    if len(phongTap) > 0:
        dict["Phòng tập"] = 1
    if len(phongTap) == 0:
        dict["Phòng tập"] = 0

    # Điền vào trang bị trong phòng
    if len(bonTam) > 0:
        dict["Bồn tắm"] = 1
    if len(bonTam) == 0:
        dict["Bồn tắm"] = 0
    if len(gheSofa) > 0:
        dict["Ghế Sofa"] = 1
    if len(gheSofa) == 0:
        dict["Ghế Sofa"] = 0

    # Điền vào số sao
    if star:
        dict["Rate Star"] = len(star)
    return dict.values()

def extract_hotel_data(hotelLinkFile: str, DataFile: str): 
    hotelFile = open(hotelLinkFile, mode="r", encoding="utf-8")
    hotelReader = csv.reader(hotelFile)
    hotelLink = list(hotelReader)[1:10]
    hotelFile.close()
    for i in hotelLink:
        print(i)
        arr = getInfor(i[0])
        append_list_as_row(DataFile, arr)
