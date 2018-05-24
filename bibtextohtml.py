#!/usr/bin/python3

"""
BibTex-to-HTML
This program is used to fill a template HTML file with information parsed
from a given BibTeX file and then store the result in a specified HTML
output file. These files are all given as command line arguments.
"""

from __future__ import print_function
import argparse
import fileinput
from shutil import copy2
import sys
import bibtexparser

"""We expect three actual arguments but they each have a flag and the first
item in argc is the program name so this totals to 7 expected items."""
EXPECTED_ARG_COUNT = 7

OPEN_BRACKETS = '{{'
CLOSE_BRACKETS = '}}'

def eprint(*args, **kwargs):
    """Prints to stderr"""
    print(*args, file=sys.stderr, **kwargs)



def get_arguments():
    """Parses the command line arguments."""

    program_description = ("Fills HTML template with information parsed from "
                           "a BibTeX file and stores the output in another HTML file.")
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument('-t', metavar='template', help='template HTML file', required=True)
    parser.add_argument('-i', metavar='inputFile', help='input BibTeX file', required=True)
    parser.add_argument('-o', metavar='outputFile', help='output HTML file', required=True)

    if len(sys.argv) != EXPECTED_ARG_COUNT:
        # Unrecoverable error if user does not supply all arguments
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Get dictionary of arguments
    args = vars(parser.parse_args())
    return args


def fill_using_template(input_filename, output_filename):
    """Parses data from input BibTeX file and uses find replace to fill those
    fields in the output file."""

    months = {"jan": "01",
              "1": "01",
              "feb" : "02",
              "2" : "02",
              "mar" : "03",
              "3" : "03",
              "apr" : "04",
              "4" : "04",
              "may" : "05",
              "5" : "05",
              "jun" : "06",
              "6" : "06",
              "jul" : "07",
              "7" : "07",
              "aug" : "08",
              "8" : "08",
              "sep" : "09",
              "9" : "09",
              "oct" : "10",
              "10" : "10",
              "nov" : "11",
              "11" : "11",
              "dec" : "12",
              "12" : "12"}

    with open(input_filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    bib_dict = bib_database.entries[0]

    with fileinput.FileInput(output_filename, inplace=True) as file:
        for line in file:
            last_found = 0
            open_bracket_location = line.find(OPEN_BRACKETS, last_found)
            close_bracket_location = line.find(CLOSE_BRACKETS, last_found)

            while open_bracket_location != -1:
                key = line[(open_bracket_location + 2):close_bracket_location]
                if key in bib_dict:
                    if key == "month":
                        line = line.replace(('{{' + key + '}}'), months[bib_dict[key]])
                    else:
                        line = line.replace(('{{' + key + '}}'), bib_dict[key])
                else:
                    eprint(key + " not found in input file.")
                last_found = close_bracket_location + 2
                open_bracket_location = line.find(OPEN_BRACKETS, last_found)
                close_bracket_location = line.find(CLOSE_BRACKETS, last_found)

            print(line, end='')


def main():
    """Open files and perform template filling."""
    args = get_arguments()

    # To start just copy everything from template into output
    copy2(args["t"], args["o"])

    fill_using_template(args["i"], args["o"])

if __name__ == "__main__":
    main()
