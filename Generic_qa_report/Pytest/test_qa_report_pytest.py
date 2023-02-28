import numpy as np
import pandas as pd
import pytest

housing_introduction = pd.read_excel("D:\\git_demo\\Generic_qa_report/Data/Housing_data.xlsx", sheet_name="introduction")

housing_sale_counts = pd.read_excel("D:\\git_demo\\Generic_qa_report/Data/Housing_data.xlsx", sheet_name="sale_counts")

housing_median_sale_price = pd.read_excel("D:\\git_demo\\Generic_qa_report/Data/Housing_data.xlsx", sheet_name="median_sale_price")

def test_sum_dwellings():
    if all(housing_sale_counts[(housing_sale_counts['All_dwelling_types']) != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats'])]):
        return False
    else:
        return True

def test_num_flats():
    if all(housing_sale_counts[(housing_sale_counts['All_dwelling_types']) < (housing_sale_counts['Flats'])]): 
        return False
    else:
        return True
    
def test_sum_dwellings_2():
   assert housing_sale_counts[(housing_sale_counts['All_dwelling_types'])] != housing_sale_counts[(housing_sale_counts['Detached'])] + housing_sale_counts[(housing_sale_counts['Semi-detached'])] + housing_sale_counts[(housing_sale_counts['Terraced'])] + housing_sale_counts[(housing_sale_counts['Flats'])]


def test_num_flats_2():
   assert housing_sale_counts[(housing_sale_counts['All_dwelling_types'])] < housing_sale_counts[(housing_sale_counts['Flats'])]

