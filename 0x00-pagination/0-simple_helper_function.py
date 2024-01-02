#!/usr/bin/env python3
"""
Write a function named index_range that
takes two integer arguments page and page_size.
"""

import pandas as pd


def index_range(page, page_size):
    """
    takes the arguments page and page_size
    """
    """
    Replace your_dataset_url_here.csv
    with the actual URL of your dataset
    """
    url="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240102T050224Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6cd37d4b726b9ca8f55207205d1e12d79be75f1e9ce185beba56613e29e2e9a5"

    """
    Read the CSV now
    """
    df = pd.read_csv(url)
    """
    get the rows in the dataframe
    """
    tr = len(df)
    """
    lets see the data now
    """
    start_index = (page - 1) * page_size
    end_index = min(page * page_size, tr)

    return start_index, end_index
