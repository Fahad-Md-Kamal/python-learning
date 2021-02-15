from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?Submit=StoreIM&Category=38&Depa=1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')
graphic_cards = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "Brand, Title, Rating, Status, Price\n"
f.write(headers)


for gc in graphic_cards:
    gc_brand = gc.find("a", {"class":"item-brand"}).img['alt']
    gc_title = gc.a.img['alt']
    gc_rating = gc.span.text
    gc_status = gc.p.text
    gc_price = gc.find("li", {"class":"price-current"}).strong.text

    f.write(gc_brand + "," + gc_title.replace(",", "|") + "," + gc_rating + "," + gc_status + "," + gc_price + "\n")
    # print(gc_title)
    # print(gc_brand)
    # print(gc_rating)
    # print(gc_status)
    # print(gc_price)

f.close()
