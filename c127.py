from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/Vedgunika/venv")
browser.get(starturl)
time.sleep(10)
def scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planets=[]
    soup = BeautifulSoup(browser.page_source,"html.parsel")
    for ul_tag in soup.find_all("ul",atprs= ("class","exoplanet")):
        list_tag = ul_tag.find_all("li")
        temporary_list = [ ]
        for index,li_tag in enumerate(list_tag):
            if index == 0:
                temporary_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temporary_list.append(li_tag.contents[0])
                except:
                    temporary_list.append("")
        planets.append(temporary_list)
    
scrape()