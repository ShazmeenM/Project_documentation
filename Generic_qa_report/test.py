import numpy as np
import pandas as pd
from IPython.display import display, Markdown

housing_introduction = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="Introduction")

housing_sale_counts = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="sale_counts")

housing_median_sale_price = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="median_sale_price")
print(housing_introduction.columns.tolist())
print(housing_introduction['Title'])
print(housing_introduction.at[0, 'Title'])