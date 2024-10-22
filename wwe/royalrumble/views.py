import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
def scrape_wwe_royal_rumble_2009():
    url = "https://www.wwe.com/superstars"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # This will find all the superstar containers (adjust if needed)
        superstar_cards = soup.find_all('img')

        players = []
        for card in superstar_cards:
            # Assuming the name is in a tag (like an h2) within the card
            name_tag = card.find('h2')  # Adjust based on actual structure
            image_tag = card.find('img')  # Find the img tag for the wrestler

            if name_tag and image_tag:
                player_info = {
                    'name': name_tag.get_text(strip=True),
                    'image_url': image_tag['src']  # Get the src attribute of the img tag
                }
                players.append(player_info)

        return players
    else:
        return []

def home(request):
    # Scrape the player names and images
    players = scrape_wwe_royal_rumble_2009()

    # Pass the players to the template
    return render(request, "royalrumble/index.html", {"players": players})
