import requests
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetches and returns HTTP headers from a specified URL.
    
    Args:
        url (str): The URL from which to fetch headers.
    
    Returns:
        dict: A dictionary containing HTTP headers.
    """
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return {}

def analyze_headers(headers):
    """
    Analyzes HTTP headers for common security-related fields.
    
    Args:
        headers (dict): A dictionary of HTTP headers.
    
    Returns:
        dict: A dictionary summarizing analysis results.
    """
    security_headers = {
        "Content-Security-Policy": headers.get("Content-Security-Policy"),
        "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
        "X-Frame-Options": headers.get("X-Frame-Options"),
        "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
        "X-XSS-Protection": headers.get("X-XSS-Protection")
    }
    return {key: value for key, value in security_headers.items() if value}

def main():
    # Example URL to analyze
    url = input("Enter a URL to analyze (include http/https): ")
    
    # Parse the URL to ensure it is valid
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Invalid URL. Please provide a valid URL including 'http://' or 'https://'.")
        return
    
    # Fetch the headers from the URL
    headers = fetch_http_headers(url)
    
    # If headers are retrieved successfully, analyze them
    if headers:
        print("\nAnalyzing HTTP Headers:")
        analysis_results = analyze_headers(headers)
        
        if analysis_results:
            for header, value in analysis_results.items():
                print(f"{header}: {value}")
        else:
            print("No security-related headers found.")
    else:
        print("Could not retrieve headers.")

if __name__ == "__main__":
    main()
```