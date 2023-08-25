# Golf Tournament Results Scraper

This Python project uses BeautifulSoup to scrape golf tournament results from a provided URL. It identifies each player and their associated team from the tournament results, finds the golf club, city, and state where the tournament took place, and uses this information to find the Course Profile on BlueGolf.com using SerpApi. It then extracts the course rating and determines if the player has two 18-hole scores from the same tournament that add up to (the course rating * 2) + 15 or less. If they do, they pass the PAT.

For each player who passes the PAT, the script lists their name, team name, the two scores that qualify them, the course where they shot the qualifying scores, and the event information (date and location of the tournament). It uses SerpApi to find the player's Instagram, Twitter, and/or LinkedIn accounts by searching their name, team/school, and the term "golf". If no social media profiles are found, it uses SerpApi to find any other type of contact information for the player, such as email or phone number.

The results are compiled into a list of players who pass the PAT, including their names, scores, courses, event information, and social profile URLs or other contact information. As the script runs, it prints out the name and scores of each player as they are checked, as well as any other relevant information or progress updates.

## Installation

1. Clone the repository
```
git clone https://github.com/yourusername/golf-tournament-results-scraper.git
```
2. Navigate to the project directory
```
cd golf-tournament-results-scraper
```
3. Install the required Python packages
```
python setup.py install
```
## Usage

Before running the script, make sure to set the environment variables `OPENAI_API_KEY` and `SERPAPI_API_KEY` in your shell.

To run the script, use the following command:
```
python main.py
```
## Debugging

For debugging, use the configuration provided in `.vscode/launch.json`.

## Dependencies

This project uses the following Python libraries:
- BeautifulSoup
- SerpApi
- OpenAI

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)