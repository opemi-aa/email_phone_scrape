# Project Title .:
Web Scraper Tool

## Description
This is a Python tool built to scrape websites and extract email addresses and phone numbers. When the tool is run, it prompts the user for the URL of the website to be scraped, and then it looks through 100 different subdomains as specified in the script after every email address and phone number. It then prints out the 100 subdomain and displays both the email and phone numbers after displaying the result. The tool creates a file for the email and phone numbers and gathers them both in a folder named "scraped_data" in the project directory.

What is Web Scraping?
Web scraping refers to the process of extracting data from websites. It involves using software tools to automate the process of gathering data from web pages.

## Key Points
Some of the key points learned from this project include:
- How to use Python for web scraping
- How to use the Beautiful Soup library to parse HTML
- How to use regular expressions to extract email addresses and phone numbers from web pages

## Getting Started
To use the web scraper tool, follow these steps:
1. Clone the repository to your local machine
2. Install the required libraries using pip install -r requirements.txt
3. Run the script by typing python email_phone_scrape.py in the command line
4. Follow the prompts to enter the URL of the website to be scraped

## Testing with a Local File
To quickly test the script's functionality with known email and phone number patterns, you can use a local HTML file.

1.  **Create a `test_page.html` file** in the project directory (`email_phone_scrape/`) with the following content:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <title>Test Page</title>
    </head>
    <body>

    <h1>Contact Us</h1>

    <p>Email: test@example.com</p>
    <p>Phone: 123-456-7890</p>
    <p>Another Phone: 0201-4638050</p>
    <p>Support: support@test.org</p>
    <p>Call us at (987) 654-3210</p>

    <a href="http://example.com/another_page.html">Another Page</a>

    </body>
    </html>
    ```

2.  **Run the script** and provide the `file://` URL to your local `test_page.html`:
    ```bash
    python email_phone_scrape.py
    ```
    When prompted, enter:
    `file:///home/kali/Documents/app-projects/email_phone_scrape/test_page.html`

    This will demonstrate the script's ability to extract the specified email addresses and phone numbers.

## Dependencies 
The following libraries are required to run the web scraper tool:
- Beautiful Soup 4
- Requests<br>You can install these libraries using pip install -r requirements.txt

## Screenshots

![Screenshot_1](https://user-images.githubusercontent.com/109806667/222299172-4d45ddb4-7e61-455e-ab5c-1e877410ed53.png)

![Screenshot_2](https://user-images.githubusercontent.com/109806667/222299198-36b18e58-aeda-4acf-9e3d-8b7e11e9689e.png)

![Screenshot_3](https://user-images.githubusercontent.com/109806667/222299215-b992d7cb-1499-47ee-8173-6e94e1557a72.png)

![Screenshot_4](https://user-images.githubusercontent.com/109806667/222296635-da3b906a-265b-4f89-8c80-6d82d1bf9a29.png)


Author
[opemi-aa]