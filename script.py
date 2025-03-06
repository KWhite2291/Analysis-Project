import requests
from bs4 import BeautifulSoup

def price_including_tax(soup: BeautifulSoup): 
    elements = soup.select(".price_color")
    first_element = elements[0]
    price = first_element.string
    if price is None: 
        price = ""

    return price 

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


def is_quantity_available(soup: BeautifulSoup): 
    elements = soup.select(".instock.availability")
    first_element = elements[0]
    quantity_available = first_element
    if quantity_available is None: 
        quantity_available = ""

    return  quantity_available

def product_description(soup: BeautifulSoup): 
    product = [p.text for p in soup.select("p") if "It's hard to imagine " in p.text]
    # first_element = elements[0]
    # product = first_element
    # if product is None: 
    #     product = ""

    return  product


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# product_page_url



# universal_product_code (upc)
table = soup.select("table")
td = soup.select("td")
print("td",td)
#print("table",table)
# book_title


titles = soup.select("div.col-sm-6.product_main > h1")
print(titles) #content_inner > article > div.row > div.col-sm-6.product_main > h1
# price_including_tax
price = price_including_tax(soup)
quantity_available = is_quantity_available(soup)
product = product_description (soup)
print(price)
print(quantity_available)
print(product)

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

