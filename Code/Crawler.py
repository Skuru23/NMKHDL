import pandas as pd

from GetCityLink import get_city_link
from GetDistrictLink import get_district_link
from GetHotelLink import get_hotel_links
from ExtractHotelLink import extract_hotel_link
from HotelExtractor import extract_hotel_data
from RemoveData import remove_data

webLink = "https://www.agoda.com/vi-vn/country/vietnam.html?cid=1844104"
cityFilePath = "../Data/city.csv"
districtFilePath = "../Data/district.csv"
townFilePath = "../Data/town.csv"
hotelFilePath = "../Data/hotel.csv"
hotelNewDataPath = "../Data/hotel_data_new.csv"
hotelDataPath = "../Data/hotel_data.csv"

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
    
    extract_hotel_link(hotelFilePath)
    
    extract_hotel_data(hotelLinkFile=hotelFilePath, DataFile= hotelNewDataPath)
    
    remove_data(hotelNewDataPath, hotelDataPath)
    
crawl_data()