from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver_path = "./chromedriver"
driver = Chrome(executable_path=driver_path)
driver.get('https://www.tred.com/buy?body_style=&distance=50&exterior_color_id=&make=&miles_max=100000&miles_min=0&model=&page_size=24&price_max=100000&price_min=0&query=&requestingPage=buy&sort=desc&sort_field=updated&status=active&year_end=2022&year_start=1998&zip=')

link_elements = driver.find_elements_by_class_name('card')

links = []

for el in link_elements:
    a_tags = el.find_elements_by_tag_name("a")
    for x in a_tags:
        href = x.get_attribute('href')
        print(href)

driver.quit()

with open('links.txt', 'w') as f:
    for link in links:
        f.write(link)
        f.write('\n')