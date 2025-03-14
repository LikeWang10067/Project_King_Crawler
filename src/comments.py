from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_comments(url, chrome_driver_path):
    chrome_options = Options()
    # run in headless mode (in the background)
    chrome_options.add_argument("--headless")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    time.sleep(3)

    comments_section = driver.find_element(By.CSS_SELECTOR, ".issuePanelContainer")

    comments = comments_section.find_elements(By.CSS_SELECTOR, ".activity-comment")

    comments_list = []

    for comment in comments:
        author = comment.find_element(By.CSS_SELECTOR, ".user-hover").text
        date = comment.find_element(By.CSS_SELECTOR, ".comment-created-date-link").text
        content = comment.find_element(By.CSS_SELECTOR, ".action-body").text
        print(f"Author: {author}\nDate: {date}\nContent: {content}\n")
        print("--------------------------------------------------")
        comments_list.append({"Author": author, "Date": date, "Content": content})

    driver.quit()

    return comments_list