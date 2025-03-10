import requests
from bs4 import BeautifulSoup
import re
import csv

url = "https://issues.apache.org/jira/browse/CAMEL-10597"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

ticket_info = {}

def extract_text(soup, label, title=None, id=None):
    element = soup.find(label, title=title, id=id)
    if element:
        next_element = element.find_next_sibling()
        if next_element:
            if title is None or '/s' not in title:
                raw_text = next_element.text
                cleaned_text = " ".join(raw_text.replace("\n", " ").split())
                return cleaned_text
            split_list = next_element.text.strip().split(", ")
            return [item.strip() for item in split_list]
    return None

# extract all the Details
details_list = ["Type", "Status", "Priority", "Resolution", "Affects Version/s", "Fix Version/s", "Component/s", "Labels", "Patch Info", "Estimated Complexity"]
for detail in details_list:
    ticket_info[detail] = extract_text(soup, "strong", detail)

# extract all the People
people_list = ["Assignee", "Reporter", "Votes", "Watchers"]
for people in people_list:
    ticket_info[people] = extract_text(soup, "dt", people)

# extract all the Dates
dates_list = ["Created", "Updated", "Resolved"]
for date in dates_list:
    ticket_info[date] = extract_text(soup, "dt")

# extract the Description
description = extract_text(soup, "div", None, "descriptionmodule_heading")
ticket_info["Description"] = description

# extract the Comments
# comments = {}
# pattern = re.compile(r"comment-\d{8}")
# ind = "comment-15748543"
# comments = soup.find_all("div", id=ind)
# comments = soup.find_all("div", class_="activity-comment")
# print(comments)

# comments_list = soup.find_all(id=ind)
# for comment in comments_list:
#     comments[comment.find("a", class_="user-hover").text] = comment.find("div", class_="action-body").text
# print("Comments: " + str(comments))
# ticket_info["Comments"] = comments

print(ticket_info)

# save the ticket_info to a .csv file
with open('ticket_info.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(ticket_info.keys())
    writer.writerow(ticket_info.values())