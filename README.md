## RSS Feed Reader

This is a cli program that takes URL of a RSS feed and prints the Title, Summary and Link
of all the entries

https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

## Motivation

I did this to practice my Python as part of [DevProjects](https://www.codementor.io/projects/tool/rss-feed-reader-in-terminal-atx32jp82q). Feedback, Questions and Pull requests are welcome.   
For major changes, please open an issue first to discuss what you would like to change.   

## Features

This RSS Reader takes RSS feed as a CLI argument or by running the program from Python REPL

## Tech/framework used

- Python 3.9

# Assumed Prerequisites

- Windows 10 Home Version 20H2
- Python 3.9 (64-bit)

# Challenges

There's no extensive testing being done.

## Installation

Use pipenv to install all the packages

## Usage

```
python reader.py http://www.feedforall.com/sample.xml
------
[Title]: RSS Solutions for Law Enforcement
[Summary]: FeedForAll helps Law Enforcement Professionals communicate with the general public and other agencies in a prompt and efficient manner. Using RSS police are able to quickly disseminate urgent and life threatening information.

Uses include:
Amber Alerts
Sex Offender Community Notification
Weather Alerts
Scheduling
Security Alerts
Police Report
Meetings
[Link]: http://www.feedforall.com/law-enforcement.htm

... and the res ...
```

```
>>> import reader.py
>>> Enter the RSS feed url (or q to quit): http://www.feedforall.com/sample.xml
# ... same as above ...
```

## Credits

- https://github.com/seraph776/rss_feed_reader
- https://github.com/3nterz/rss-feed-reader


## License
[MIT](https://choosealicense.com/licenses/mit/) © [LeanKhan](https://github.com/LeanKhan)