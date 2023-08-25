```python
class Tournament:
    def __init__(self, name, date, location, golf_club, city, state):
        self.name = name
        self.date = date
        self.location = location
        self.golf_club = golf_club
        self.city = city
        self.state = state
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players

    def get_tournament_info(self):
        return {
            "name": self.name,
            "date": self.date,
            "location": self.location,
            "golf_club": self.golf_club,
            "city": self.city,
            "state": self.state
        }
```