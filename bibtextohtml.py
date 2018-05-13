#!/usr/bin/python3

"""
BibTex-to-HTML
This program is used to fill a template HTML file with information parsed
from a given BibTeX file and then store the result in a specified HTML
output file. These files are all given as command line arguments.
"""

import sys


def print_help_text():
    """Prints usage text to console."""
    helptext = """
    Usage: bibtextohtml [OPTION...]
    bibtextohtml fills HTML templates with info from BibTeX files.

      Example:
       bibtextohtml -t "template.html" -i "input.bib" -o "output.html"

      Options:
       -t     template HTML file
       -i     input BibTeX file
       -o     output HTML file
    """

    print(helptext)


def main():
    """Read in command line arguments and perform template filling."""
    if len(sys.argv) != 3:
        print_help_text()


if __name__ == "__main__":
    main()
