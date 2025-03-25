import requests
from bs4 import BeautifulSoup

def extract_description(soup: BeautifulSoup):
  # you could also use the select method but it would return a list (no need because ids are unique)
  div_tag = soup.find(id="product_description")  # find by id
  paragraph_tag = div_tag.find_next("p")  # find sibling paragraph (it's at the same level as div tag)
  description = paragraph_tag.get_text(strip=True)  # get human readable text (strip=True => remove new lines or whitespace at start and end)
  return description

def extract_value(soup: BeautifulSoup, selector: str):
    elements = soup.select(selector)
    first_element = elements[0]
    text = first_element.get_text(strip=True)  # get human readable text
    return text

def extract_url(soup: BeautifulSoup, selector: str):
    elements = soup.select(selector)
    first_element = elements[0]
    text = first_element.get_text(strip=True)
    return text 

def extract_td_value(soup: BeautifulSoup):
    td_value = soup.find("td").text
    return td_value


def extract_rating(soup: BeautifulSoup):
    rating_tag = soup.find("p").text
    return rating_tag

def extract_image_url(soup):
    return soup.find('img')['src']



url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

td_value = extract_td_value(soup)
title = extract_value(soup,".col-sm-6.product_main > h1")
price = extract_value(soup, ".price_color")
quantity_available = extract_value(soup, ".instock.availability")
description = extract_description(soup)
category_name = soup.find("a").text.strip()
rating = extract_rating(soup)
image_url = soup.find("img").text.strip()

book = {"title": title, "price": price, "url": url, "quantity_available": quantity_available, "description": description, "category_name": category_name, "rating": rating, "image_url": image_url}
books = []

print(book)











