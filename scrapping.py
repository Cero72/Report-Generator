import requests
from bs4 import BeautifulSoup
from apis import links

import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    try:
        # Send GET request to the webpage
        headers = {'User-Agent': 'Mozilla/5.0'}  # Adding user-agent header to mimic a browser
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract main text content from specific tags (e.g., <p>, <div>, <article>)
            text_elements = soup.find_all(['p'])
            
            # Extract text from each element and concatenate
            extracted_text = ' '.join(element.get_text(separator='\n', strip=True) for element in text_elements)
            
            return extracted_text
        else:
            print("Error:", response.status_code)
            return None
    except requests.HTTPError as e:
        print("HTTP error occurred:", e)
        return None
    except Exception as e:
        print("Error occurred:", e)
        return None

def scrape_multiple_links(links):
    all_text = []
    for link in links:
        text = scrape_data(link)
        if text:
            all_text.append(text)
    return all_text

# Example usage:
links = links

all_text = scrape_multiple_links(links)
for idx, text in enumerate(all_text, start=1):
    print(f"Text from link {idx}:")
    try:
        # Print the text using UTF-8 encoding
        print(text.encode('utf-8'))
    except UnicodeEncodeError:
        # If unable to encode, print a message indicating inability to encode
        print("Unable to encode text due to Unicode characters")
    print("=" * 50)
