'''

This application is designed to extract a set of features from a specified HTML
document and output them to a specified text file.

Usage: python app.py url output_file
To Test: python test.py

'''

# import system specific parameter module
import sys
# import web scraper module
from webscraper import WebScraper
# import content writing module
from contentwriter import ContentWriter
# import helper methods module
from helpers import *

args = sys.argv[1:] # arguments passed by user

# program should not execute if the wrong number of arguments are passed
if len(args) is not 2:
    raise Exception(
        "Wrong number of arguments\nUsage: python app.py url output_file.txt"
    )

url = args[0]
output = args[1]

# attempt to read the web page and extract data to output file
try:
    scraper = WebScraper(url)
    file = ContentWriter(output)

    links = list_to_multi_line(scraper.get_dom_links())
    tags = list_to_line(scraper.get_dom_tags())
    sequences = list_to_multi_line(scraper.get_dom_sequences())

    file.generate_content(links, tags, sequences)
    file.write()

# prompt use with error if something goes wrong
except Exception as err:
    print(err)
