import sys
import numpy as np
import pandas as pd
import xarray as xr

#TODO read from http://xarray.pydata.org/en/stable/quick-overview.html
#pd may have an auto read: https://github.com/jharman25/ama-parser/blob/master/ama_parser/ama_parser.py
def main():
    if len(sys.argv) != 3:
        print("Required both arguments: raw text input and comma separated coordinates")
        sys.exit(1)
    raw_in = sys.argv[1]
    coordinates = sys.argv[2]
    load_raw_input(raw_in)


def load_raw_input(raw_in):
    print("Loading raw input: " + raw_in)
    with open(raw_in) as f:
        lines = f.readlines()[3:]
        for line in lines:
            print(line)


if __name__ == '__main__':
    main()
