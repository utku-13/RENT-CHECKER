from sheety_main import SheetySetter
from web_scraping import WebScraper
from datetime import datetime as dt
from webdri import WebDriverr


current_time = dt.now().strftime("%d/%m/%Y")
#dont forget it gives different time lines date.

s = SheetySetter()
w = WebScraper()
we = WebDriverr()

main_dict = w.take_rent_datas()


#it gives 3 (each of em includes 9 elems) different params as the dictionary.


#OOP works quite fine.

for n in range(9):
    a = main_dict["title_names"][n]
    b = main_dict["addrs_names"][n]
    c = main_dict["link_lists"][n]
    we.sendkeys(a,b,c)

#bunlari tek tek giricez. send keys ile.