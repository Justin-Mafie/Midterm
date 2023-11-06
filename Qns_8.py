import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page for US counties
url = "https://en.wikipedia.org/wiki/County_(United_States)"

try:
    # Send a GET request to fetch the web page content
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links on the page
        links = soup.find_all('a')

        # Create a list to store link addresses with 'New York' in the text
        new_york_links = []

        # Iterate through the links and filter those containing 'New York' in the text
        for link in links:
            link_text = link.text
            if 'New York' in link_text:
                link_address = link.get('href', 'No href attribute')
                new_york_links.append((link_text, link_address))

        # Write the link addresses to a file named 'new York.txt'
        with open('new York.txt', 'w', encoding='utf-8') as file:
            for text, address in new_york_links:
                file.write(f'Text: {text}\nAddress: {address}\n\n')

        print("Links with 'New York' in text have been saved to 'new York.txt'")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
