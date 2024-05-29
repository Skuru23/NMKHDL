import pandas as pd

from GetCityLink import get_city_link
from GetDistrictLink import get_district_link
from GetTownLink import get_town_link

webLink = "https://www.agoda.com/vi-vn/country/vietnam.html?cid=1844104"
cityFilePath = "./Data/city.csv"
districtFilePath = "../Data/district.csv"
townFilePath = "../Data/town.csv"

def crawl_data():
    # cityLink = get_city_link(webLink)
    # city = pd.DataFrame(cityLink)
    # city.to_csv(cityFilePath,index=False)
    
    # districtLink = get_district_link(cityFilePath)
    # district = pd.DataFrame(districtLink)
    # district.to_csv(districtFilePath, index=False)
    
    townLink = get_town_link(districtFilePath)
    town = pd.DataFrame(townLink)
    town.to_csv(townFilePath, index=False)
    
crawl_data()