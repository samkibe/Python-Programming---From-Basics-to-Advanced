print("Web Scrapping using BeautifulSoup \n")
 
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.your_target_webserver=target+server")
print(response) 
# print(response.content) 
print(response.status_code) #proceed if it is 200, 404 means server not found

# #bonus
# card = soup.find_all("img") or links, or etc etc
# soup = BeautifulSoup(response.content, "html.parser")

# cards = soup.find_all("div", attrs = {"class":"your_card"})
# # or

# your_card_item = card.find("div",attrs = {"class":"your_card"})
# print(your_card_item) #etc etc