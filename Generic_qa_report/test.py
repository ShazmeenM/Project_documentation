import numpy as np
import pandas as pd
from IPython.display import display, Markdown

housing_introduction = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="introduction")

housing_sale_counts = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="sale_counts")

housing_median_sale_price = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="median_sale_price")

print(housing_introduction.columns.tolist())
print(housing_introduction['Column_a'])
print(housing_introduction.at[0, 'Column_a'])
print(housing_sale_counts.columns.tolist())

print(housing_sale_counts.isnull())
print(housing_sale_counts.isnull().sum())

n_missing = print(housing_sale_counts.isnull().values.sum())

df2 = housing_sale_counts.dropna(how='all').dropna(how='all', axis=1)
print(df2)
print(df2.isnull())
print(df2.isnull().any())


print(housing_sale_counts.isnull().values.sum())
print(housing_sale_counts[housing_sale_counts['Detached'].isnull()])