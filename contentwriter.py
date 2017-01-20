""" Module defines classes writing content to a file """

# import regular expression module
import re

class ContentWriter:
    """ This class is used to handle the making and writing of an output file """

    def __init__(self, output):
        self.output = output
        self.validate_output()
        self.content = ""

    def validate_output(self):
        """ Validates that the output filename given is a valid .txt filename """
        file_name_pattern = r"^[_a-zA-Z0-9\\-\\.]+(txt|TXT)$" 
        if not re.match(file_name_pattern, self.output):
            raise Exception('Please enter a valid output file name')

    def generate_content(self, *sections):
        """ Given the strings passed, returns strings seperated by a spacer string """
        self.content = '\n\n...\n\n'.join(list(sections))

    def write(self):
        """ Writes content to the objects specified output filename """
        file = open(self.output, "w", encoding='utf-8')
        file.write(self.content)
        file.close()
