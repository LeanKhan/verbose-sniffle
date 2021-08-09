""" project: CLI RSS Feed Reader
	created: 9-08-21, @author: leankhan (eslean20@gmail.com)
"""
import feedparser
import sys
import lxml.html
import lxml.html.clean

def parser(url: str) -> None:
	"""
	Gets the url as string, parses it and returns it!
	"""

	if url:

		rss_source = feedparser.parse(url)

		if len(rss_source.entries) == 0:
				print('Invalid URL :/')
		else:
			rss_length = len(rss_source.entries)
			for i in range(1, rss_length):
				rss_content = rss_source.entries[i]

				print('\n-------------')
				print("""[Title]: {0}\n[Summary]: {1}\n[Link]: {2}"""\
					.format(rss_content.title, clean_html(rss_content.summary), rss_content.link))

def get_url_input() -> None:
	"""
	Get URL from user
	"""
	run = True
	while run:
		url = input("Enter the RSS feed url (or q to quit): ")

		if url.lower() == "q":
			run = False
			print("Bye!")
			break
		elif url:
			parser(url)

def clean_html(text: str) -> str:
	"""
	Returns text without HTML tags
	>>> clean_html("<i>Fresh guy :)</i>")
	'Fresh guy :)'
	"""
	txt = lxml.html.fromstring(text)
	cleaner = lxml.html.clean.Cleaner(style=True)
	return cleaner.clean_html(txt).text_content()

def main() -> None:
	get_url_input()

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		parser(sys.argv[1])
	else:
		print('No URL provided :/')
else:
	main()