import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetches HTTP headers from a given URL and returns them in a dictionary format.
    
    Parameters:
    url (str): The target URL to analyze.

    Returns:
    dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return {}

def extract_domain_info(url):
    """
    Extracts domain and scheme from the given URL.

    Parameters:
    url (str): The target URL to analyze.

    Returns:
    tuple: A tuple containing the domain and scheme.
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc, parsed_url.scheme

def display_headers(headers):
    """
    Displays the HTTP headers in a readable format.

    Parameters:
    headers (dict): The HTTP headers to display.
    """
    print("\nHTTP Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")

def main():
    """
    Main function to execute the OSINT tool.
    Prompts the user for a URL and retrieves HTTP headers.
    """
    url = input("Enter a URL (e.g., http://example.com): ")
    
    # Extract domain information
    domain, scheme = extract_domain_info(url)
    print(f"\nAnalyzing {domain} with scheme {scheme}...\n")
    
    # Get HTTP headers
    headers = get_http_headers(url)
    
    # Display the headers if any were retrieved
    if headers:
        display_headers(headers)
    else:
        print("No headers retrieved.")

if __name__ == "__main__":
    main()
```