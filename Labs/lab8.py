import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://viseartparis.com/collections/all-products").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("a", {"class":"card-information__text h4"})
title = span.text
#tags = soup.findAll("a", {"class":re.compile("(text)")})
#for card in tags:
   # a = card.findAll("card-information__text h4",{"class":"a"})
    #print(a)
span = soup.find("span", {"class":"price-item--regular"})
price = span.text
print("Item %s costs %s" % (title, price))