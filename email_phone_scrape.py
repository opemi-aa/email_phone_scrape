import os
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

# Create the directory to store the scraped data if it does not already exist
if not os.path.exists("scraped_data"):
    os.makedirs("scraped_data")

user_url = str(input('[+] Enter Target URL To Scan: '))
urls = deque([user_url])

scraped_urls = set()
emails = set()
phone_numbers = set()

count = 0
try:
    while len(urls):
        count += 1
        if count == 100:
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        new_phone_numbers = set(re.findall(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", response.text))
        phone_numbers.update(new_phone_numbers)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

# Create a file to store the scraped email addresses
with open("scraped_data/emails.txt", "w") as f:
    print("[+] Scraped Emails:")
    for email in emails:
        f.write(email + "\n")
        print(email)

# Create a file to store the scraped phone numbers
with open("scraped_data/phone_numbers.txt", "w") as f:
    print("\n[+] Scraped Phone Numbers:")
    for phone_number in phone_numbers:
        f.write(phone_number + "\n")
        print(phone_number)

print("\n[+] Scraped data saved in 'scraped_data' folder.")