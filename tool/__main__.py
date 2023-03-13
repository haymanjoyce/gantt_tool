#!/usr/bin/env python3

"""Entry point script."""
# tool/__main__.py

from tool import cli

import typer
import svg
import pandas as pd


def packages():
    print('\nPackages:\n')
    print("'svg' from PyPI for programmatically creating SVG mark up (alt: 'drawsvg2')")
    print("'pandas' from PyPI for reading CSV files and more (alt: 'openpyxl')")
    print("'typer' from PyPI for developing the CLI (alt: 'argparse')")
    print("'colorama' from PyPI for coloured terminal text (possible 'typer' dependency)")
    print("'shellingham' from PyPI for detecting the shell (possible 'typer' dependency)")
    print("'pytest' from PyPI is a unit test framework")
    print('"pyinstaller" from PyPI for turning the application into an executable (not imported)')


def read_file(file):
    df = pd.read_csv(file)
    print(df)


def main():
    print(cli.__name__)


# if module run as script
if __name__ == '__main__':
    main()

