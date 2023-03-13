#!/usr/bin/env python3

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


if __name__ == '__main__':
    packages()
    # read_file("/Users/richard/Desktop/sample.csv")
