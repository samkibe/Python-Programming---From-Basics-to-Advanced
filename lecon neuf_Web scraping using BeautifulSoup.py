print("Web Scrapping using BeautifulSoup")

# to use BeautifulSoup install it through cmd
# 1st install requests - pip install requests
# 2nd install BeautifulSoup - pip install BeautifulSoup4
 
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.jumia.co.ke/catalog/?q=finance+novels")
print(response) #<Response [200]> - means we have got a response from the server
# print(response.content) 
print(response.status_code) #proceed if its 200, 404 means server not found

soup = BeautifulSoup(response.content, "html.parser")
# # print(soup)
#print(soup.prettify())

# find('a')
# find_all("img"), div
# find_parent("a")
# find_next_siblings("a")

# card = soup.find_all("img")
cards = soup.find_all("div", attrs = {"class":""})

for card in cards:

	price = card.find("div",attrs = {"class":""})
	# print(price.text)
	title = card.find("span",attrs = {"class":""})
	# print(title.text.strip("\n"))
	pages = card.find("div",attrs = {"class":""})
	# print(pages.text)
	author = card.find("div",attrs = {"class":""})
	# print(author.text)

# data = "{} {} {} {}".format(price.text,title.text.strip("\n"),pages.text,author.text)
data = "{} {} {} {}".format(price,title,pages,author) #prints none because i have not identified any container or class
print(data, "\n")


# Database access 
# sqlite

import sqlite3
# sqlite3.connect("kibepy.db")
conn = sqlite3.connect("kibepy.db")
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY,NAME TEXT, SALARY REAL) """)
# c.execute("INSERT INTO EMP(ID,NAME,SALARY)VALUES(101,'ABC',100000)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY)VALUES(102,'EFG',200000)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY)VALUES(103,'HIJ',150000)")
# c.execute("INSERT INTO EMP(ID,NAME,SALARY)VALUES(104,'KLM',100500)")
# conn.execute("COMMIT")

c.execute("""SELECT * FROM EMP""")
# print(next(c))

for row in c:
	print(row)

c.execute("UPDATE EMP SET SALARY = 650000 WHERE ID =102")
conn.execute("COMMIT")
c.execute("""SELECT * FROM EMP WHERE ID = 102""")
# print(next(c))

c.execute("DELETE FROM EMP WHERE ID = 101")
conn.execute("COMMIT")
