```python
class Course:
    def __init__(self, name, city, state, profile_url):
        self.name = name
        self.city = city
        self.state = state
        self.profile_url = profile_url
        self.rating = None

    def extract_course_rating(self, soup):
        """
        Extracts the course rating from the BeautifulSoup object of the course profile page.
        """
        try:
            rating_section = soup.find('div', {'class': 'course-rating-section'})
            self.rating = float(rating_section.find('span', {'class': 'rating'}).text)
        except Exception as e:
            print(f"Failed to extract course rating for {self.name}. Error: {str(e)}")
            self.rating = None
```