```python
class Player:
    def __init__(self, name, team, scores, tournament):
        self.name = name
        self.team = team
        self.scores = scores
        self.tournament = tournament
        self.social_profiles = None
        self.contact_info = None

    def check_PAT_pass(self, course_rating):
        for i in range(len(self.scores) - 1):
            for j in range(i + 1, len(self.scores)):
                if self.scores[i] + self.scores[j] <= (course_rating * 2) + 15:
                    return True, self.scores[i], self.scores[j]
        return False, None, None

    def set_social_profiles(self, social_profiles):
        self.social_profiles = social_profiles

    def set_contact_info(self, contact_info):
        self.contact_info = contact_info

    def get_info(self):
        return {
            "name": self.name,
            "team": self.team,
            "scores": self.scores,
            "tournament": self.tournament,
            "social_profiles": self.social_profiles,
            "contact_info": self.contact_info
        }
```