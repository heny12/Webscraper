""" This module contains functionality for testing the webscraper program """

# import unit testing module
import unittest
# import web scraper module
from webscraper import WebScraper
# import content writing module
from contentwriter import ContentWriter
# import helper methods module
from helpers import *
# import operating system interfaces for checking/removing files
import os

TEST_URL = 'http://pitchbook.com'
TEST_OUTPUT = 'test.txt'

class WebscraperTest(unittest.TestCase):

    def test_create_webscraper(self):
        self.assertTrue(
            WebScraper(TEST_URL),
            "should create webscraper object"
        )

    def test_get_dom_tags(self):
        webscraper = WebScraper(TEST_URL)
        tags = webscraper.get_dom_tags()
        self.assertIsNotNone(
            tags,
            "should get dom tags from url"
        )

    def test_get_dom_links(self):
        webscraper = WebScraper(TEST_URL)
        links = webscraper.get_dom_links()
        self.assertIsNotNone(
            links,
            "should get links from url"
        )

    def test_get_dom_sequences(self):
        webscraper = WebScraper(TEST_URL)
        sequences = webscraper.get_dom_sequences()
        self.assertIsNotNone(
            sequences,
            "should get dom sequences from url"
        )

    def test_validate_url(self):
        self.assertRaises(
            Exception, WebScraper, 'not a valid url .com',
            'should raise Exception when an invalid url is passed'
        )

    def test_gather_child_node_dom_tags(self):
        webscraper = WebScraper(TEST_URL)
        tags = WebScraper.gather_child_node_dom_tags(webscraper.dom.html)
        self.assertIsNotNone(
            tags,
            "should get node tags of all children"
        )

class ContentTest(unittest.TestCase):
    def test_create_content_writer(self):
        self.assertTrue(
            ContentWriter(TEST_OUTPUT),
            "should create content writer object"
        )

    def test_validate_output(self):
        self.assertRaises(
            Exception, ContentWriter, 'invalid.output.pdf',
            "should raise Exception when an invalid output filename is given"
        )

    def test_generate_content(self):
        writer = ContentWriter(TEST_OUTPUT)
        sample_text = "hello world"
        writer.generate_content(sample_text, sample_text, sample_text)
        expected_output = "hello world\n\n...\n\nhello world\n\n...\n\nhello world"
        self.assertEqual(
            writer.content, expected_output,
            "should generate correctly formated output string"
        )

    def test_write(self):
        # ensure file doesnt already exist
        if os.path.exists(TEST_OUTPUT):
            os.remove(TEST_OUTPUT)
        ContentWriter(TEST_OUTPUT).write()
        self.assertTrue(
            os.path.exists(TEST_OUTPUT),
            "should create an output file"
        )
        os.remove(TEST_OUTPUT) # remove test file once complete

class HelpersTest(unittest.TestCase):
    def test_list_to_line(self):
        lst = ['a', 'b', 'c', 'd']
        expected_output = "abcd"
        self.assertEqual(
            list_to_line(lst), expected_output,
            "list should be joined into single line"
        )

    def test_list_to_multi_line(self):
        lst = ['a', 'b', 'c', 'd']
        expected_output = "a\nb\nc\nd"
        self.assertEqual(
            list_to_multi_line(lst), expected_output,
            "list should be joined into multiple lines"
        )

    def test_get_valid_words(self):
        text = "hello w-rld foo 1234 @# a bar _wam_"
        expected_output = ['hello', 'foo', 'bar']
        self.assertEqual(
            get_valid_words(text), expected_output,
            "should only get valid words from text"
        )

    def test_word_sequences(self):
        text = "Hello World foo Foo foo Bar FOO Wam"
        expected_output = ['Hello World', 'Bar FOO Wam']
        self.assertEqual(
            word_sequences(text), expected_output,
            "should extract titlecase word sequences from text"
        )

# run tests
if __name__ == '__main__':
    unittest.main()
