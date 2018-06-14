#!/usr/bin/env python3

import glob
import re
import sys

# Regex to remove all HTML tags
removeTagRegex = r"<[^>]+>"
# Matches <br>
brRegex = r"<br>"
placeholder = "PlAcEhOlDeR"
# Regex for multiple <br> in a row, maybe with line break
lotsOfBreaks = r"(<br>\n*){2,}"



if __name__ == '__main__':
    # Pass file as parameter on command line
    path = sys.argv[1]
    # Get the file contents
    myFile = open(path, "r")
    contents = myFile.read()
    # Swap <br> with a placeholder, so won't be removed with all other tags
    contents = re.sub(brRegex, placeholder, contents)
    # Search and remove all HTML tags
    noTags = re.sub(removeTagRegex, "", contents)
    # Put back line breaks
    noTags = re.sub(placeholder, "<br>", noTags)
    # Remove extraneous line breaks
    noTags = re.sub(lotsOfBreaks, "<br>\n", noTags)
    myFile.close()
    myFile = open(path, "w")
    # Add so TiddlyWiki will render as Tiddler, not text
    myFile.write("type: text/vnd.tiddlywiki\n\n")
    myFile.write(noTags)
    myFile.close()
