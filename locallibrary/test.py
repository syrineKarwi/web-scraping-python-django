from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen as uRep

import requests


page = requests.get("https://www.mytek.tn/13-pc-portable")
soup = BeautifulSoup(page.text, 'lxml')
section = soup.findAll('div', {'class':"product_img_link"})
print(soup.section.findAll('a'))
