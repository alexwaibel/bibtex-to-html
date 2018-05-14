#!/usr/bin/python3

"""
BibTex-to-HTML
This program is used to fill a template HTML file with information parsed
from a given BibTeX file and then store the result in a specified HTML
output file. These files are all given as command line arguments.
"""

import argparse
import fileinput
from shutil import copy2
import sys
import bibtexparser

"""We expect three actual arguments but they each have a flag and the first
item in argc is the program name so this totals to 7 expected items."""
EXPECTED_ARG_COUNT = 7


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

    with open(input_filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)


    bib_dict = bib_database.entries[0]

    """
    This is a horrible solution. The runtime of this is bad and I'll have to
    come back to it later and figure out something with regex so I don't have
    to go through the output file a million times.
    """
    for item in bib_dict:
        fixed_item = "{{" + item + "}}"
        with fileinput.FileInput(output_filename, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(fixed_item, bib_dict[item]), end='')


def main():
    """Open files and perform template filling."""
    args = get_arguments()


    # To start just copy everything from template into output
    copy2(args["t"], args["o"])

    fill_using_template(args["i"], args["o"])

if __name__ == "__main__":
    main()
