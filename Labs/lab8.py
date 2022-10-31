import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://viseartparis.com/collections/all-products").content
soup = BeautifulSoup(data, 'html.parser')
items = soup.find_all("div", {"class":"card-information__wrapper"})

for item in items:

#title = span.text
#tags = soup.findAll("a", {"class":re.compile("(text)")})
#for card in tags:
   # a = card.findAll("card-information__text h4",{"class":"a"})
    #print(a)
    price = item.find("span", {"class":"money"}).text
    name = item.find("a", {"class":"card-information__text"}).text
    #print("Item %s costs %s" % (, price))
    print(price, name)