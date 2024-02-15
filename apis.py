import requests
from keys import base, apikey, search_id

# Define the API endpoint
base_url = base
# Define the required query parameters
api_key = apikey
search_engine_id = search_id

query = "canoo company overview"
# Construct the API request URL with query parameters
api_url = f"{base_url}?key={api_key}&cx={search_engine_id}&q={query}"

# Send an HTTP GET request to the API endpoint
response = requests.get(api_url)

# List to store the links
links = []

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    search_results = response.json()
    # Extract and store the links
    for item in search_results.get('items', []):
        links.append(item['link'])
else:
    print("Error:", response.status_code)


print(links)