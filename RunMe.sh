#! /bin/bash

# Usage definition
# Adapted from https://stackoverflow.com/questions/16483119/an-example-of-how-to-use-getopts-in-bash#16496491
usage() { echo "Usage: $0 myfile.ext" 1>&2; exit 1; }

# Check that an argument was passed
if [ -z "$1" ]; then
    usage
fi

# Remove temporary files?
flag=0

# Get name and extension seperately
basename=$(basename "$1")
extension="${basename##*.}"
filename="${basename%.*}"

echo $1

# Make extension all lower case
extensionLowerCase="$(echo "$extension" | tr '[:upper:]' '[:lower:]')"

# Pandoc can't read PDF, so convert to html
if [ "$extensionLowerCase" = "pdf" ]
then
    # Run pdf2htmlEX
    echo "Converting PDF to HTML..."
    docker run -ti --rm -v "${PWD}":/pdf bwits/pdf2htmlex pdf2htmlEX "$1" "$filename".html
    basename="$filename".html
    flag=1
fi


# Convert file via Pandoc
# "+RTS -K102400000 -RTS" to not get a stack overflow
echo "Converting to WikiText..."
pandoc +RTS -K102400000 -RTS -t wikitext.lua "$1" -o "$filename".tid


# Remove .html file if we converted it from a PDF
if [ "$flag" = 1 ]
then
    echo "Removing temporary files..."
    # Need -f because pdf2htmlEX write-protects the file
    rm -f "$basename"
fi

# Run tiddlyify to clean up the file and add type needed for proper import
echo "Cleaning up WikiText..."
./tiddlify.py "$filename".tid
echo "Done!"
