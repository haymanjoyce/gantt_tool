#!/usr/bin/env python3

import argparse

import pandas
import svg
import pandas as pd


def packages():
    print("argparse from Standard Library (alt: typer)")
    print("svg from PyPI for programmatically creating SVG mark up (alt: drawsvg2)")
    print("pandas from PyPI for reading CSV and Excel files (alt: openpyxl")


def read_file(file):
    df = pd.read_csv(file)
    print(df)


if __name__ == '__main__':
    packages()
    # read_file("/Users/richard/Desktop/sample.csv")
