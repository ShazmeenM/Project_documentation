import numpy as np
import pandas as pd
import pytest

housing_introduction = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="introduction")

housing_sale_counts = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="sale_counts")

housing_median_sale_price = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="median_sale_price")


def test_greater_equal():
   num = 100
   assert num >= 100
   
# content of test_assert1.py
def f():
    return housing_sale_counts['Flats'].any()


def test_function():
    assert f() > housing_sale_counts['All_dwelling_types'].any()


def test_sum_dwellings():
   
    if housing_sale_counts['All_dwelling_types'].all != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']).all:
        return False
    else:
        return True

def test_less():
   all_dwelling_types = housing_sale_counts['All_dwelling_types']
   flats = housing_sale_counts['Flats']
   assert all_dwelling_types.any() < flats.any()

def test_less_d():
   num = 100
   assert num < 50

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

print(test_uppercase())

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

print(test_some_primes())

# test_capitalize.py

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
    
import pytest

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)

def test_greater():
   num = 100
   assert num > 100

def test_greater_equal():
   num = 100
   assert num >= 100
