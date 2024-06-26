import requests
from bs4 import BeautifulSoup

def scrape_restaurants(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch the webpage")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    print("HTML content fetched and parsed successfully")

    # Debugging statement: print a small portion of the HTML to verify its content
    print(soup.prettify()[:1000])

    restaurants = []

    # Find all div elements with class 'restaurant-info'
    for restaurant in soup.find_all('div', class_='restaurant-info'):
        name_elem = restaurant.find('h4', class_='restaurant-name')  # Find h4 element with class 'restaurant-name'
        rating_elem = restaurant.find('span', class_='restaurant-rating')  # Find span element with class 'restaurant-rating'

        if name_elem and rating_elem:
            name = name_elem.text.strip()  # Extract and strip text from name element
            rating = rating_elem.text.strip()  # Extract and strip text from rating element
            restaurants.append({'name': name, 'rating': rating})
        else:
            print("Failed to find name or rating for a restaurant")

    return restaurants

url = 'https://www.freshmenu.com/mumbai'
restaurants = scrape_restaurants(url)

if restaurants:
    for restaurant in restaurants:
        print(f"Restaurant: {restaurant['name']}, Rating: {restaurant['rating']}")
else:
    print("No restaurants found or error occurred")
