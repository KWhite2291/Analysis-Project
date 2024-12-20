import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"






page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# product_page_url
# universal_product_code (upc)
# book_title
titles = soup.select("#content_inner > article > div.row > div.col-sm-6.product_main > h1")
print(titles) #content_inner > article > div.row > div.col-sm-6.product_main > h1
# price_including_tax
# identify the variable and define it
# 1 price
# 2 assign the price a value hardcoding a literal
# 3 price = 51.77
# print(price) 
# grab the body and assign it to price
# price = soup.select("body")
# price_excluding_tax
# quantity_available
# product_description
# category
# review_rating
# image_url

