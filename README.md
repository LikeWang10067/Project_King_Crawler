# Project_King_Crawler
This project is created for the purpose of crawling data from Apache Camel project.

---

## Features

- Extracts ticket details such as Type, Status, Priority, Resolution, and more.
- Extracts ticket people info like Assignee, Reporter, Votes, and Watchers.
- Extracts ticket date info like Created, Updated, and Resolved.
- Extracts the ticket description.
- (On the way) Extracts the ticket comments.
- Export the result to a .csv file

---

### **Command-Line Options**
The script supports the following command-line options:

| Option            | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `-u`, `--url`     | Change the url of the ticket that the user wants to extract data            |


---

### **Default Settings**
- **URL**: `https://issues.apache.org/jira/browse/CAMEL-10597`

If you want to change the default settings, use the `-u` option.

---

### **Examples**

1. **Run the script with default JIRA ticket:**
   ```bash
   python tickets_crawler.py
   ```

2. **Run the script with a JIRA ticket URL:**
   ```bash
   python tickets_crawler.py -u "https://issues.apache.org/jira/browse/CAMEL-10598"
   ```

---

## **Output**
The script generates a report of the ticket: -> into a .csv file.

---

## **Requirements**
- Python 3.x
- `requests` library (install via `pip install requests`)
- `bs4` library (install via `pip install bs4`)

---

## **License**
I am lazy and don't have a lot of time left, I "promise" I will get a License later when needed. ^_^

---

## **Contributing**
Welcome to join me, even if it's a project for fun, please open an issue or submit a pull request for any improvements or bug fixes.

---

## **Contact**
For questions or feedback, please contact Like Wang at like.wang@mail.utoronto.ca.

---