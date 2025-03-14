import requests
from bs4 import BeautifulSoup
import csv
import comments as cms

def init(url, comments_flag, chrome_driver_path):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch page")
        exit(1)
    raw_text = response.text
    soup = BeautifulSoup(raw_text, 'html.parser')
    ticket_info = data_crawling(soup)
    if comments_flag:
        # extract the Comments
        comments_list = cms.get_comments(url, chrome_driver_path)
        ticket_info["Comments"] = comments_list
    write_to_csv(ticket_info)


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

def data_crawling(soup):
    ticket_info = {}
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

    return ticket_info

def write_to_csv(ticket_info):
    with open('ticket_info.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(ticket_info.keys())
        writer.writerow(ticket_info.values())

if __name__ == "__main__":
    import getopt, sys
    def usage():
        print("Usage:")
        print("Options:")
        print("\t-h, --help: Print this help message")
        print("\t-u, --url: URL of the JIRA ticket")
        print("\t-c, --comments: Flag to extract comments")
        print("\t-p, --chrome_driver_path: Path to the Chrome Driver")
        print('Note:')
        print('\tThe default value for the URL is "https://issues.apache.org/jira/browse/CAMEL-10597"')
        print('\tThe default value for the comments flag is False')
        print('\tThe default value for the Chrome Driver path is "/usr/local/bin/chromedriver", it\'s the default path for macOS, it might be different for other OS')
        print("Example:")
        print("\tpython tickets_crawler.py")
        print("\tpython tickets_crawler.py -u https://issues.apache.org/jira/browse/CAMEL-10597 -c -p /usr/local/bin/chromedriver")
        sys.exit(0)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcu:p:", ["help", "url", "comments", "chrome_driver_path"])
    except getopt.GetoptError as err:
        print(err)
    url = "https://issues.apache.org/jira/browse/CAMEL-10597"
    comments_flag = False
    chrome_driver_path = "/usr/local/bin/chromedriver"
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        if opt in ("-u", "--url"):
            url = arg
        if opt in ("-c", "--comments"):
            comments_flag = True
        if opt in ("-p", "--chrome_driver_path"):
            chrome_driver_path = arg
    init(url, comments_flag, chrome_driver_path)