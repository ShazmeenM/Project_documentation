import numpy as np
import pandas as pd


housing_introduction = pd.read_excel("D:\\git_demo\\Generic_qa_report/Data/Housing_data.xlsx", sheet_name="introduction")
housing_sale_counts = pd.read_excel("D:\\git_demo\\Generic_qa_report/Data/Housing_data.xlsx", sheet_name="sale_counts")
housing_median_sale_price = pd.read_excel("D:\\git_demo\\Generic_qa_report/Data/Housing_data.xlsx", sheet_name="median_sale_price")

def test_num_flats():
    print("Description: Checks if values of a variable are always less than other.")  
    print("Data specific description: Checks if the number of flats are lesser than the number of all other dwelling types in all councils.")  
    if all(housing_sale_counts[(housing_sale_counts['All_dwelling_types']) <(housing_sale_counts['Flats'])]): 
        print("Status: Fail. A fail means number of flats are not less than all other dwelling types in atleast one council.")
        return False
    else:
        print("Status: Pass. A pass means number of flats are less than all other dwelling types in all councils")
        return True
print (test_num_flats())
housing_sale_counts[(housing_sale_counts['All_dwelling_types']) < (housing_sale_counts['Flats'])]

test_neg = ((housing_sale_counts['Detached' or 'Semi-detached' or 'Terraced' or 'Flats']) < 0).any()
print ("Status:")
print (test_neg)
print("Status description: A true means there is a negative values (Fail). A false means there is no negative value (Pass).")
housing_sale_counts[((housing_sale_counts['Flats']) < 0)]  

# Assumption
Location: 
Quality:
Sensitivity Score:
Long description: Total number of detached houses in a local authority are greater than total number of flats.
