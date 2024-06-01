import pandas as pd

from GetCityLink import get_city_link
from GetDistrictLink import get_district_link
from GetHotelLink import get_hotel_links

webLink = "https://www.agoda.com/vi-vn/country/vietnam.html?cid=1844104"
cityFilePath = "../Data/city.csv"
districtFilePath = "../Data/district.csv"
townFilePath = "../Data/town.csv"
hotelFilePath = "../Data/hotel.csv"

def crawl_data():
    cityLink = get_city_link(webLink)
    city = pd.DataFrame(cityLink)
    city.to_csv(cityFilePath,index=False)
    
    districtLink = get_district_link(cityFilePath)
    district = pd.DataFrame(districtLink)
    district.to_csv(districtFilePath, index=False)

    hotelLink = get_hotel_links(districtFilePath)
    hotel = pd.DataFrame(hotelLink)
    hotel.to_csv(hotelFilePath, index= False)
    
crawl_data()