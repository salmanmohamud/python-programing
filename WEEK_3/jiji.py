import requests
import csv 
from bs4 import BeautifulSoup

url="https://greenspoon.co.ke/sale/"

response = requests.get(url)

if response.status_code != 200:
    print(" Scrape Failed")
    print(response.status_code)
else:
    soup = BeautifulSoup(response.content, 'html.parser')
    lists = soup.find_all("ul", class_="products columns-3")
    items = lists[0].find_all("div", class_='uael-woo-product-wrapper')
    Data =[]
    for item in items:
        category = item.find('span', class_="uael-woo-product-category").text.strip()
        title = item.find('h2', class_="woocommerce-loop-product__title").text
        price = item.find('bdi').text
        Data.append({"Category":category,"Title":title,"Price":price})

        print("-------------------")
        print("Category: ", category)
        print("Title: ", title)
        print("Price: ", price)
        print("-------------------")

    with open("Main.csv","w",newline="",encoding="utf-8") as csvfile:
        names=["Category", "Title", "Price"]
        writer=csv.DictWriter(csvfile,fieldnames=names)
        writer.writeheader()
        writer.writerows(Data)