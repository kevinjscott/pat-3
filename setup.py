from setuptools import setup, find_packages

setup(
    name='golf_tournament_scraper',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'serpapi',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'golf_tournament_scraper = main:main',
        ],
    },
    url='https://github.com/user/golf_tournament_scraper',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python project to scrape golf tournament results, identify players who pass the PAT, and find their contact information.'
)