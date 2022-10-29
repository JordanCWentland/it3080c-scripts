#This script requests information regarding a product page on the mechanical keyboard store kbdfans.com
#made by Wentlajc - Jordan Wentland

#Imports for bs4 and requests modules.
from bs4 import BeautifulSoup
import requests, re 

#request the site and return the text format of the site.
webData = requests.get("https://kbdfans.com/collections/diy-kit/products/kbdfans-x-lazurite-d60lite").text

#Parse the web data via Beautiful soup.
soup = BeautifulSoup(webData, 'html.parser')

#Find the selected items within the request, and format appropriately.
itemTitle = soup.find("h1", {"class":"product-detail__title small-title"}).text
itemPrice = soup.find("span", {"class":"theme-money large-title"}).text
itemStock = soup.find ("button", {"class": "btn btn--secondary"}).text.lower().strip()

#Conditional statement to check if item is in stock and update the itemStock value. 
if itemStock == "add to cart":
    itemStock = "in stock!"
else:
    itemStock = "out of stock!"

#Print the requests items using f-strings
print(f"{itemTitle} costs {itemPrice}. This item is currently {itemStock} ")