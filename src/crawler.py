import requests
from bs4 import BeautifulSoup

url = "https://issues.apache.org/jira/browse/CAMEL-10597"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# extract data test
title = soup.find("h1").text

# extract Status
status = soup.find("strong", text="Status:")
if status:
    status_val = status.find_next_sibling().text.strip()
    print(status_val)

