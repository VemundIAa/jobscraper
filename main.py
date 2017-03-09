import requests as rq
from bs4 import BeautifulSoup as bs
import datetime
import os
from requests.compat import urljoin


keywords = ["nyutdannet", "nyutdannede", "angular", "frontend", "front-end", "python", "apputvikling",
            "systemutvikler","artificial intelligence", "kunstig intelligens", "machine learning"]
r = rq.get("https://m.finn.no/job/fulltime/search.html?extent=3947&location=0.20001&location=1.20001.20013&location=1.20001.20061&occupation=0.23")

date = datetime.date.today()
today = date.strftime("%Y_%d_%m")

filename = today+".txt"
newfile = open(filename, "w+")

seen = []
soup = bs(r.text,"html.parser")
results = soup.find("div", {"class": "line flex align-items-stretch wrap cols1upto480 cols2upto990 cols3from990"})

links = results.findAll("div", {"class": "unit flex align-items-stretch result-item"})

for item in links:
    item_href = item.find("a").attrs["href"]
    print("Link found:", item_href)
    url = urljoin("https://m.finn.no", item_href)
    ad = rq.get(url)
    new_soup = bs(ad.text,"html.parser")
    description = new_soup.find("div",{"class": "object-description mbl"})
    contents = "".join(str(item) for item in description.contents)
    i = 0
    for keyword in keywords:
        isSubstring = keyword in contents

        if isSubstring == True and i == 0:
            newfile.write("\n"+url+ "\t"+ keyword)
            i += 1


        elif isSubstring == True and i == 1:
            newfile.write("\t"+keyword)
            i = 1













