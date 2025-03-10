import requests
from bs4 import BeautifulSoup

url = "https://issues.apache.org/jira/browse/CAMEL-10597"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# extract data test
title = soup.find("h1").text
print("Ticket Title: " + title)

ticket_info = {}

def extract_details_text(soup, label):
    element = soup.find("strong", title=label)
    if element:
        next_element = element.find_next_sibling()
        if next_element:
            if "/s" in label:
                split_list = next_element.text.strip().split(", ")
                return [item.strip() for item in split_list]
            return next_element.text.strip()
    return None

# extract all the Details
type_ = extract_details_text(soup, "Type")
ticket_info["Type"] = type_
status = extract_details_text(soup, "Status")
ticket_info["Status"] = status
priority = extract_details_text(soup, "Priority")
ticket_info["Priority"] = priority
resolution = extract_details_text(soup, "Resolution")
ticket_info["Resolution"] = resolution
affects_version = extract_details_text(soup, "Affects Version/s")
ticket_info["Affects Version/s"] = affects_version
fix_version = extract_details_text(soup, "Fix Version/s")
ticket_info["Fix Version/s"] = fix_version
component = extract_details_text(soup, "Component/s")
ticket_info["Component/s"] = component
labels = extract_details_text(soup, "Labels")
ticket_info["Labels"] = labels
patch_info = extract_details_text(soup, "Patch Info")
ticket_info["Patch Info"] = patch_info
estimated_complexity = extract_details_text(soup, "Estimated Complexity")
ticket_info["Estimated Complexity"] = estimated_complexity

print(ticket_info)