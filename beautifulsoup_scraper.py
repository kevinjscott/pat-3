```python
from bs4 import BeautifulSoup
import requests
from player import Player
from tournament import Tournament

def scrape_tournament_results(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    tournaments = []

    # Assuming the website has a table structure for the data
    for row in soup.find_all('tr'):
        columns = row.find_all('td')

        # Assuming the first column is player name and second column is team name
        player_name = columns[0].text.strip()
        team_name = columns[1].text.strip()

        # Assuming the third column is golf club, fourth is city and fifth is state
        golf_club = columns[2].text.strip()
        city = columns[3].text.strip()
        state = columns[4].text.strip()

        # Assuming the sixth column is tournament date and seventh is tournament location
        tournament_date = columns[5].text.strip()
        tournament_location = columns[6].text.strip()

        # Assuming the eighth and ninth columns are the two 18-hole scores
        score1 = int(columns[7].text.strip())
        score2 = int(columns[8].text.strip())

        player = Player(player_name, team_name, score1, score2)
        players.append(player)

        tournament = Tournament(golf_club, city, state, tournament_date, tournament_location)
        tournaments.append(tournament)

    return players, tournaments
```