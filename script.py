import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')


#print(soup)
titles = soup.select("#content_inner > article > div.row > div.col-sm-6.product_main > h1")
print(titles) #content_inner > article > div.row > div.col-sm-6.product_main > h1
