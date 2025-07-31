import requests
from bs4 import BeautifulSoup
import tldextract
import re

# Function to extract HTTP headers
def get_http_headers(url):
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to extract email addresses from a webpage
def extract_emails(html_content):
    # Regular expression to find email addresses
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_regex, html_content)

# Function to scrape a webpage and extract information
def scrape_website(url):
    headers = get_http_headers(url)
    if headers:
        print(f"HTTP Headers for {url}:")
        for key, value in headers.items():
            print(f"{key}: {value}")

    try:
        # Fetch the webpage content
        response = requests.get(url)
        html_content = response.text
        
        # Extract emails from the webpage
        emails = extract_emails(html_content)
        if emails:
            print(f"Email addresses found on {url}: {', '.join(emails)}")
        else:
            print(f"No email addresses found on {url}.")

    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

# The main function to execute the script
if __name__ == "__main__":
    # Example URL for testing (can be replaced with user input)
    target_url = 'https://example.com'
    
    # Extract domain information
    extracted = tldextract.extract(target_url)
    print(f"Scanning domain: {extracted.domain}.{extracted.suffix}")
    
    # Start scraping the website
    scrape_website(target_url)
```