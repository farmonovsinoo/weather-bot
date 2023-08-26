import requests
from bs4 import BeautifulSoup as bs

def Toshkent():
    toshkent = requests.get("https://sinoptik.ua/погода-ташкент")
    html = bs(toshkent.content, 'html.parser')
    for tosh in html.select("#content"):
        min = tosh.select(".temperature .min")[0].text
        max = tosh.select(".temperature .max")[0].text
    return min[4:], max[5:]

def Buxoro():
    buxoro = requests.get("https://sinoptik.ua/погода-бухара")
    html = bs(buxoro.content, 'html.parser')
    for bux in html.select("#content"):
        min = bux.select(".temperature .min")[0].text
        max = bux.select(".temperature .max")[0].text
    return min[4:], max[5:]

def Samarqand():
    samarqand = requests.get("https://sinoptik.ua/погода-Caмapкaнд")
    html = bs(samarqand.content, 'html.parser')
    for sam in html.select("#content"):
        min = sam.select(".temperature .min")[0].text
        max = sam.select(".temperature .max")[0].text
    return min[4:], max[5:]