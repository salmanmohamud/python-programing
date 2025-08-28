import requests
from bs4 import BeautifulSoup
# step 1: send a request to the website
url = "https://quotes.toscrape.com/"
# step2: parse the HTML content
response = requests.get(url)
#step 3: get the satus code and labeling more friendly output
if response.status_code == 200:
    print("Fetched successfully")
else:
    print("Error")             

# step4: using the find or findall to extract info from the web

soup= BeautifulSoup(response.text, "html.parser")

# one= soup.find("div", class_ ="quote")
# step5: now we using the find to print tags as example also if you want only to see the body tex without the HTML
one= soup.find("div", class_ ="tags")
print(one.text)

#STEP6: for findall to get the text we need to loop through to access them individually





























