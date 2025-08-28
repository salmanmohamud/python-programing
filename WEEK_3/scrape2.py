





import requests
from bs4 import BeautifulSoup

# inserting the url of website u scaping and asking to request url
url ="https://en.wikipedia.org/wiki/List_of_banks_in_Kenya#Microfinance_banks"
response = requests.get(url)

# naming the error or the success in understandable terms
if response.status_code == 200:
    print("Fetched successfully")
else:
    print("Error")

# storing all the content of website in variable called soup
soup = BeautifulSoup(response.text,"html.parser")
# storing all the content of the specific div class in variable called main
main = soup.find("div",class_="mw-content-ltr mw-parser-output" )
#print(main)
# storing all the content of the unordered list from the div class in another variable called items
items=main.find("ul")
#print(main)
# storing all the contents of the list in the un onordered list in another variable called links
links= items.find_all("li") 
#creating aloop to print the list one by one until it completes printing all the names in the linst
for link in links:
 print(link.text)