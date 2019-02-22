import requests
from bs4 import BeautifulSoup
import re

def search_weburl(search):
  try:
    searched_items = []

    page = requests.get(search)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    products = soup.findAll("div",class_=re.compile("product-item-details"))
    # print products[0]
    for product in products:
      try:
        details = {}
        
        # name
        details['name'] = product.find('a',class_=re.compile("product-item-link")).text
        
        # Link
        temp_hodler = product.find('a',class_=re.compile("product-item-link"))
        if temp_hodler['href']:
          details['url'] = temp_hodler['href']
        else:
          details['url'] = None

        searched_items.append(details)
        
      except Exception as e:
        pass


    return searched_items
    
  except Exception as e:
    pass
