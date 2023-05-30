ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55790511507858%2C%22east%22%3A-122.32650557894577%2C%22south%22%3A37.66392932357855%2C%22north%22%3A37.829799336489636%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A574104%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

import requests
from bs4 import BeautifulSoup


#every web site dont give these infos in every condition.
#so you must set headers sometimes.
#https://httpbin.org/headers this web site will show everything you need to know.
HEADERS = {
    "User-Agent": "USER-AGENT",
    "Accept": "YOUR-ACCEPT"
}
class WebScraper:
    def take_rent_datas(self):
        response = requests.get(url=ZILLOW_URL,headers=HEADERS)
        data = response.content
        soup = BeautifulSoup(data, "html.parser")
        # soup = BeautifulSoup(data, "html.parser")
        # print(soup.prettify())

        # head = soup.find_all(name="a")
        # print(head)
        title_names = []
        place_titles = soup.select('[data-test="property-card-price"]')
        for title in place_titles:
            title_names.append(title.text)

        addrs_names = []
        addres =soup.select('[data-test="property-card-addr"]')
        for add in addres:
            addrs_names.append(add.text)
        link_lists = []
        links = soup.select('a[data-test="property-card-link"].property-card-link')
        for link in links[0::2]:
            link_house = link.get("href")
            if "https://www.zillow.com/" in link_house:
                link_lists.append(link_house)
            else:
                print(f"https://www.zillow.com{link_house}")
        finaldict = {
            "title_names":title_names,
            "addrs_names":addrs_names,
            "link_lists":link_lists
        }
        return finaldict

    #code scrapes every element that we wanted from website.