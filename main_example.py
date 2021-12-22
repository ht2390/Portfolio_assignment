
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt
import os

import numpy as np

import pandas as pd
import matplotlib as plt

import util


def author():
    return 'your name here please'

def main():
    """ Main program """
    # Code goes over here.
    orders_file = "orders-01.csv"
    orders_df = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan'])
    orders_df = orders_df.sort_values(by = 'Date')
    start_date = orders_df.index[0]
    end_date = orders_df.index[-1]
    Symbol_list = orders_df['Symbol'].unique()


    path = util.symbol_to_path('IBM', '/Users/allentang/Desktop/ford_project/')

    price = util.get_data(Symbol_list, pd.date_range(start_date, end_date))


if __name__ == "__main__":
    main()