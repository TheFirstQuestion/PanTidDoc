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
    fullpath = sys.argv[2].split(".")[-2]

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
    noTags = re.sub(lotsOfBreaks, "<br><br>\n\n", noTags)
    myFile.close()

    # Add metedata to file
    myFile = open(path, "w")
    # Filename skipping .tid, in title case
    filename = path[:-4].title()
    # Get folder names
    tags = fullpath.split("/")
    # Take out ../
    while ".." in tags:
        tags.remove("..")
    # Remove last tag, which is the filename itself
    del tags[-1]
    # Format tags: [tag] [tag] [tag]
    tagsString = ""
    for t in tags:
        tagsString += "[[" + t + "]] "

    # Add title of file to become title of Tiddler
    # excluding .tid extension
    myFile.write("title: " + filename + "\n")
    # Add the tags
    myFile.write("tags: " + tagsString + "\n")

    # Add so TiddlyWiki will render as Tiddler, not text
    # Not needed if have title attribute
    #myFile.write("type: text/vnd.tiddlywiki\n\n")

    # To separate metadata and data
    myFile.write("\n\n")


    # Add link to the actual file (in WikiText)
    myFile.write("//This file is located at: ''" + sys.argv[2] + "''//\n\n\n")
    # Add horizontal line
    myFile.write("---\n")
    # Write data
    myFile.write(noTags)

    myFile.close()
