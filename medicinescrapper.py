import ssl
import mysql.connector
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="123456",
database="shops"
)

selectcursor = mydb.cursor(buffered=True)
insertcursor = mydb.cursor(buffered=True)

# Get All Companies List
selectcursor.execute("""CREATE TABLE `category_ranges` (
  `id` int(6) NOT NULL PRIMARY KEY,
  `start` int(11) NOT NULL DEFAULT 1,
  `end` int(11) NOT NULL DEFAULT 1,
  `link` varchar(255),
  `status` enum('pending','running','completed','failed') NOT NULL DEFAULT 'pending'
)""")

selectcursor.execute("SELECT id, link FROM category_ranges WHERE link IS NOT NULL ORDER BY id")

myresult = selectcursor.fetchall()

for x in myresult:
    company_id = x[0]
    company_link = x[1]

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # url = input("Enter URL-")
    url = company_link

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags page link
    tags = soup.find_all ("a", class_="alphaSubcat")

    for tag in tags:
        sql = "INSERT IGNORE INTO sub_categories (name, category_id) VALUES (%s, %s)"
        val = (tag.text, str(company_id))
        insertcursor.execute(sql, val)
        mydb.commit()
        print(insertcursor.rowcount, "record inserted.")

    sleep(2.4)
