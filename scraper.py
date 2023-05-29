try:
    import requests
    from bs4 import BeautifulSoup

    # The URL of the news site we're going to scrape
    URL = "https://news.ycombinator.com/"

    # Send a GET request to the URL
    response = requests.get(URL)

    # Print the status code of the response
    print(f"Response status code: {response.status_code}")

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    print(soup.prettify())  # This line should be here

    # Find the news headlines on the page
    headlines = soup.select("span.titleline > a")

    # Print out the headlines
    print(f"Number of headlines found: {len(headlines)}")
    for headline in headlines:
        print(headline.text)

except Exception as e:
    print(f"An error occurred: {e}")
