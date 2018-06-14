# PanTidDoc

_Convert virtually any file (including PDFs) to a tiddler--edit it, search it, quote it, transclude it._

## Description

I frequently encounter files that I want to include in my personal wiki. TiddlyWiki can embed files, but you can't really _do_ anything with them. I wanted a way to transform my files into tiddlers to be able to utilize all the great features of TiddlyWiki.

This script is my solution. First, the script checks if the input file is a PDF _(RunMe.sh)_. Because Pandoc cannot convert PDFs, the PDF is converted to HTML by pdf2htmlEX _(RunMe.sh)_. The resulting file (or the original file, if not a PDF) is then converted to WikiText through a custom writer for Pandoc _(wikitext.lua)_. Finally, the WikiText is cleaned up and encoded for proper importing into TiddlyWiki _(tiddlify.py)_.

## Requirements

* [pandoc](http://pandoc.org/): `sudo apt-get install pandoc`
* [pdf2htmlEX](https://coolwanglu.github.io/pdf2htmlEX/) (required only for PDFs):
  * [Install Docker](https://www.docker.com/community-edition#/download)
  * [Install pdf2htmlEX as a Docker container](https://hub.docker.com/r/bwits/pdf2htmlex/)
  * [Allow Docker to run without `sudo`](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo#)


## Usage
`./RunMe.sh filename.ext`


## Contributing

If you have found a bug or have suggestions for improvements, please open an issue. Feel free to fork this repository and hack it however you wish. PanTidDoc is a work in progress, and thus very far from perfect.
