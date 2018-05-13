#!/usr/bin/python3

"""
BibTex-to-HTML
This program is used to fill a template HTML file with information parsed
from a given BibTeX file and then store the result in a specified HTML
output file. These files are all given as command line arguments.
"""

import argparse
import sys


def open_files():
    """Opens files given as command line arguments."""
    program_description = ("Fills HTML template with information parsed from "
                           "a BibTeX file and stores the output in another HTML file.")
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument('-t', metavar='template', help='template HTML file', required=True)
    parser.add_argument('-i', metavar='inputFile', help='input BibTeX file', required=True)
    parser.add_argument('-o', metavar='outputFile', help='output HTML file', required=True)

    if len(sys.argv) != 4:
        parser.print_help()


def main():
    """Perform template filling."""
    open_files()


if __name__ == "__main__":
    main()
