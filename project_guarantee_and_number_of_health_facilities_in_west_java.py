# -*- coding: utf-8 -*-
"""Project Guarantee and Number of Health Facilities in West Java.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S9cY_M1Rcsuv85Bh28tGh3cS3KcnD0wL
"""

import pandas as pd

jamkes = pd.read_csv("Jaminan Kesehatan Jabar.xlsx - data.csv")
jamkes.info()

jamkes

faskes = pd.read_csv("Jumlah Faskes Jabar.xlsx - data.csv")
faskes.info()

faskes