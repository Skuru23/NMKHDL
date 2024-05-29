from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from helium import *
import pandas as pd

driver = webdriver.Chrome()

dsachTP = [
    "https://www.agoda.com/vi-vn/search?city=13170&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221357&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=88775&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=2758&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115695&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=234333&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=222717&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=222377&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=228720&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221815&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=232720&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=16440&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=17190&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216927&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216371&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=233219&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=15932&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=218905&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223982&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=215718&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=215714&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=232259&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=226346&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220864&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221359&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221974&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224558&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=229784&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224677&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=2679&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115652&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220971&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=231195&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=728008&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=219949&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220855&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=232764&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223444&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220969&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=16552&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=215303&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221396&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221674&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221745&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=21673&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224114&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216898&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=16264&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220856&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216625&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224934&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=215683&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=3738&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=219320&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=215197&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=17160&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=106068&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=18865&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=226104&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=218925&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=227145&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=17161&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=17243&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220870&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223174&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=17245&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=16079&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220514&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=78908&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220863&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=105661&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115756&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=230898&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=18866&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=228387&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=719776&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204060&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=234568&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=229505&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=227246&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=222761&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=226146&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=225104&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=21557&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=669620&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=231375&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220871&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=230398&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115740&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115735&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=232995&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204066&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=19603&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=219731&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=219537&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=226263&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=18044&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223237&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220906&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=218499&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=218121&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=230218&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=217097&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=217051&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=232772&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=230985&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=728010&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=105991&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=702291&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223230&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=229586&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216211&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216465&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=669642&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=233232&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204068&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=17162&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115622&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=231976&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=728002&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=228632&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115678&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=718883&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=231650&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=233407&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=106067&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=231205&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=78906&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223243&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115625&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=720973&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204056&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220366&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204057&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=226062&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=228115&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=214967&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=219881&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=219886&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=225825&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216281&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=737290&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=720974&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204054&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204059&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=229817&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216614&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=222832&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204063&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224382&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224345&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221016&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=728014&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=229464&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=217290&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220859&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220860&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115635&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220862&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=230916&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204067&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223849&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=223145&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=225574&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115734&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115754&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=231414&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115751&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204064&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224933&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115629&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204055&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204071&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204065&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=227720&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115753&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220858&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115657&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115663&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115661&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=115748&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204061&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204053&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=218832&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=728007&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=216225&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=204070&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=220109&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=227612&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=728005&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=221899&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=214897&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=215124&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=232804&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
    "https://www.agoda.com/vi-vn/search?city=224649&checkIn= 2020-11-15&los=1&rooms=1&adults=2&children=0&sort=priceLowToHigh",
]


def getLinkHotel():
    authors = []
    for i in dsachTP:
        print("Đang ở trong thành phố " + i)
        a = 0
        page = 1
        driver.get(i)
        sleep(5)
        while a == 0:
            print("Đang ở trang số: " + strs(page))
            click(Point(0, 0))
            sleep(2)
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                # Scroll down to the bottom.
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Wait to load the page
                sleep(2)
                # Calculate new scroll height and compare with last height.
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                sleep(2)
            sleep(30)
            htmltext = driver.page_source
            soup = BeautifulSoup(htmltext, "html.parser")
            links = soup.findAll("a", class_="PropertyCard__Link")
            for x in links:
                try:
                    link = "https://www.agoda.com" + x["href"]
                    authors.append(link)
                    print(link)
                except:
                    print("Không có thẻ href")
            print("Có tát cả " + strs(len(links)) + " khách sạn")
            try:
                driver.find_element_by_id("paginationNext").click()
                page = page + 1
            except:
                print("Hết trang, sang khu vực kế tiếp")
                a = 1
        sleep(2)
    return authors


hotel = getLinkHotel()
print("Tất cả hotel: ")
print(hotel)
print(len(hotel))
hotel = pd.DataFrame(hotel)
hotel.to_csv("../Data/hotel.csv", index=False)
