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

def test_2(func):
    def wrapper(the_number):
        print("Checks if sum of columns equals total")
        return func(the_number)
    return wrapper
@test_2
def test_2(num):
    if num<0:
 
        return ("Negative")
    
    if num>0:
 
        return ("Positive")
 
    return ("The number is 0")

print(test_2(6))


    
def Test_1(num):
    if num<0:
 
        return ("Negative")
    
    if num>0:
 
        return ("Positive")
 
    return ("The number is 0")

print(Test_1(6))


def test_sum_dwellings(housing_sale_counts):
    if (housing_sale_counts['All_dwelling_types']) == (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']):
        return True
    else:
        return False

print(test_sum_dwellings(housing_sale_counts.all()))

def test_sum_dwellingss(housing_sale_counts):
    if (housing_sale_counts['All_dwelling_types']) == (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']):
        print("Great")
    else:
        print("Sorry for asking...")
        
print(test_sum_dwellingss(housing_sale_counts.all()))

print(np.count_nonzero((housing_sale_counts['All_dwelling_types']) != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats'])))
print(np.where((housing_sale_counts['All_dwelling_types']) != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats'])))
print(list(zip(*np.where((housing_sale_counts['All_dwelling_types']) != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats'])))))

def test_sum_dwellings():
    print("Description: Checks if sum of columns equals total.")  
    print("Long Description: Checks if sum of detahced, semi-detached, terraced and flats equals all dwelling types")  
    if housing_sale_counts['All_dwelling_types'].all != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']).all():
        print("Status: Fail. A fail means sum of columns do not equal total.")
        return False
    else:
        print("Status: Pass. A pass means sum of columns equals total.")
        return True
print (test_sum_dwellings())

def test_sum_dwellings():
    print("Description: Checks if sum of variables equals total.")  
    print("Data specific description: Checks if sum of detahced, semi-detached, terraced and flats equals all dwelling types")  
    if housing_sale_counts['All_dwelling_types'].all != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']).all:
        print("Status: Fail. A fail means sum of varaibles do not equal total.")
        return False
    else:
        print("Status: Pass. A pass means sum of variables equals total.")
        return True
print (test_sum_dwellings())

def test_num_flats():
    print("Description: Checks if values of a variable are always less than other.")  
    print("Data specific description: Checks if the number of flats are always lesser than the number of all other dwelling types.")  
    if all(housing_sale_counts['Detached' or 'Semi-detached' or 'Terraced']) > all(housing_sale_counts['Flats']): 
        print("Status: Pass. A pass means number of flats are less than all other dwelling types in all the councils.")
        return True
    else:
        print("Status: Fail. A fail means number of flats are not less than all other dwelling types in atleast one council.")
        return False
print (test_num_flats())

test_neg = ((housing_sale_counts['Detached' or 'Semi-detached' or 'Terraced' or 'Flats']) < 0).any().any()
print ("Status:")
print (test_neg)
print("Status description: A true means there is a negative values (Fail). A false means there is no negative value (Pass).")

test_neg = ((housing_median_sale_price['Detached' or 'Semi-detached' or 'Terraced' or 'Flats']) < 0).any().any()
print ("Status:")
print (test_neg)
print("Status description: A true means there is a negative values (Fail). A false means there is no negative value (Pass).")
