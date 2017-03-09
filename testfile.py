import requests as rq
from bs4 import BeautifulSoup as bs
import os
import datetime
from requests.compat import urljoin

while i < 3:
    keywords = ["nyutdannet", "nyutdannede", "angular", "frontend", "front-end"]
    r = rq.get("https://m.finn.no/job/fulltime/search.html?extent=3947&location=0.20001&location=1.20001.20013&location=1.20001.20061&occupation=0.23")

    date = datetime.date.today()
    today = date.strftime("%Y_%d_%m")

    filename = today+".txt"
    newfile = open(filename, "w+")

    if not os.path.isdir(today):
        os.makedirs(today)

    soup = bs(r.text,"html.parser")
    results = soup.find("div", {"class": "line flex align-items-stretch wrap cols1upto480 cols2upto990 cols3from990"})

    links = results.findAll("div", {"class": "unit flex align-items-stretch result-item"})

    for item in links:
        item_href = item.find("a").attrs["href"]
        print("Link found:", item_href)
        ad = rq.get(urljoin("https://m.finn.no", item_href))
        new_soup = bs(ad.text,"html.parser")
        description = new_soup.find("div",{"class": "object-description mbl"})
        contents = "".join(str(item) for item in description.contents)

        for keyword in keywords:
            i = 1
            isSubstring = keyword in contents

            if isSubstring == True:
                newfile.write("\n"+keyword+":   "+ urljoin("https://m.finn.no", item_href))




    i += 1


#test = rq.get("https://m.finn.no/job/fulltime/ad.html?finnkode=91975280")
#print(test.text)


