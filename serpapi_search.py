```python
import os
from serpapi import GoogleSearch

def find_course_profile(golf_club, city, state):
    params = {
        "q": f"{golf_club} {city} {state} BlueGolf.com Course Profile",
        "location": "United States",
        "api_key": os.getenv("SERPAPI_API_KEY"),
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    try:
        course_profile_url = results['organic_results'][0]['link']
    except IndexError:
        course_profile_url = None

    return course_profile_url

def find_social_profiles(player_name, team_name):
    params = {
        "q": f"{player_name} {team_name} golf Instagram Twitter LinkedIn",
        "location": "United States",
        "api_key": os.getenv("SERPAPI_API_KEY"),
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    social_profiles = {}
    for result in results.get('organic_results', []):
        link = result['link']
        if 'instagram.com' in link:
            social_profiles['instagram'] = link
        elif 'twitter.com' in link:
            social_profiles['twitter'] = link
        elif 'linkedin.com' in link:
            social_profiles['linkedin'] = link

    return social_profiles if social_profiles else None
```