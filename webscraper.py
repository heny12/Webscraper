""" Module defines classes used for scraping web pages """

# import regular expression module
import re
# import module for opening URLs
from urllib.request import urlopen
# import BeautifulSoup html parser module
from bs4 import BeautifulSoup
# import helper methods module
from helpers import *

class WebScraper:
    """
    This class provides functionality for scraping a web page and extracting
    certain data from that page
    """

    def __init__(self, url):
        self.url = url
        self.validate_url()
        self.raw_html = urlopen(self.url).read()
        self.dom = BeautifulSoup(self.raw_html, 'html.parser')

    def get_dom_tags(self):
        """
        Extracts list of raw HTML tags contained in the web page
        in the order in which they appear
        """
        return WebScraper.gather_child_node_dom_tags(self.dom.html)

    def get_dom_links(self):
        """ Extracts list of all links embedded within the HTML page """
        links = []
        # get link from each link tag
        for link in self.dom.find_all('a', href=True):
            link = str(link.get('href'))
            links.append(link)
        return links

    def get_dom_sequences(self):
        """
        Extracts list of all sequences of two or more words that have
        the first letter capitalized
        """
        sequences = []
        # iterates over all text within dom
        for text in self.dom.find_all(text=True):
            # only gather sequences which are displayed on the page,
            # not comments, styles, etc...
            if (text.parent.name not in ['title', 'script', 'head', '[document]', 'style'] and
                                 not re.match('<!--.*-->', str(text.encode('utf-8')))):
                valid_words = get_valid_words(text)
                valid_word_sequences = word_sequences(' '.join(valid_words))
                sequences.extend(valid_word_sequences)
        return sequences

    def validate_url(self):
        """ Validates that a url can be read, raising an exception if not """
        try:
            urlopen(self.url)
        except Exception as err:
            raise Exception('Please enter a valid URL ' + str(err))

    @staticmethod
    def gather_child_node_dom_tags(node):
        """
        Recursivly navigates a dom node, generating a list of the raw html
        tags in their relative order in the document
        """
        tree = []
        # continue of node is a dom tag
        if node.name is not None:
            # if tag has children get those tags and surround those with the
            # parent tags
            if len(node.contents) > 0:
                for child in node.contents:
                    tree.extend(WebScraper.gather_child_node_dom_tags(child))
            tree = ['<'+str(node.name)+'>'] + tree + ['</'+str(node.name)+'>']
        return tree
