"""
This program converts data clip to a MySQL data seed file.

Opens CSV cleans up the data and then outputs to a 

By Rich Budek 03/05/2020 in Python 3.8
"""


import pandas as pd
import numpy as np
import jinja2
import math
import re


class Config_Data:
    #set up by user once
    filepath = "Z:\Shared Folders\Data\Per\Proj\Prog\Proj-SalesTracker\SalesTracker"
    filename_orders = "Orders.xls"
    filename_packing = "PackingSlip.xlsx"
    filename_sales = "Sales.xls"
    filename_target = "Targets.xlsx"


class Project_Data:
    #data that gets transferred between functions
    full_filename_orders = ""
    file_orders_is_csv = False

    full_filename_packing = ""
    file_orders_is_csv = False

    full_filename_sales = ""
    file_sales_is_csv = False

    full_filename_target = ""
    file_target_is_csv = False


class Sale_In:
    order_num = 0
    name = ""
    type = ""
    amt_quote = 0.0
    order_date_str = ""
    order_date_val = 0
    ship_date_str = ""
    ship_date_val = 0

