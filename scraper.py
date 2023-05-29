import requests
from bs4 import BeautifulSoup

# The URL of the news site we're going to scrape
URL = "https://news.ycombinator.com/"

# Send a GET request to the URL
response = requests.get(URL)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the news headlines on the page
headlines = soup.find_all("a", class_="storylink")

# Print out the headlines
for headline in headlines:
    print(headline.text)



