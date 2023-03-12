import requests
from bs4 import BeautifulSoup

# make http request from the code
url = "http://books.toscrape.com/index.html"
response = requests.get(url)

# get html as text
html = response.content

# feed it to parser
scraped = BeautifulSoup(html, "html.parser")

"""
# prints the title tag and its content
print(scraped.title)

# get the text from an element
print(scraped.title.text)
# exactly the same outcome
scraped.find("title")

# same but strips the text from all invisible characters
title_text = scraped.title.text.strip()
print(title_text)


# we use underscore with class here because class is a reserved name in Python,
# but class is also something used in html, so in order to avoid confusion we use class_
# however other html names are used without underscore
link = scraped.find("article", class_="product_pod").h3.a
print(link.text.strip())

# to retrieve information from a single element
link_text = scraped.article.h3.a["title"]
print(link_text)
"""

articles = scraped.find_all("article", class_="product_pod")
# print(articles)
# the type of articles is a list, so we can iterate over it
# print(type(articles))

# for article in articles:
#     print(article.h3.a["title"])

# prices = scraped.find_all("p", class_="price_color")
# print(prices)
#
# def average_price():
#     total = 0
#     for price in prices:
#         price = float(price.text[1:])
#         total += price
#     print(total)
#     average_prices = total / len(prices)
#     print(average_prices)
#
# average_price()

result = []
for article in articles:
    title = article.h3.a["title"]
    price = article.find("div", class_="product_price").find("p", "price_color")
    price = (price.text[1:])
    result.append({title:price})
print(result)