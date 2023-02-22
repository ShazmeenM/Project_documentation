import numpy as np
import pandas as pd
from IPython.display import display, Markdown

housing_introduction = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="introduction")

housing_sale_counts = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="sale_counts")

housing_median_sale_price = pd.read_excel("D:\\git_demo\\Generic_qa_report/Housing_data.xlsx", sheet_name="median_sale_price")
    
    
housing_sale_counts['total'] = housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']
print(housing_sale_counts.columns.tolist())
housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']

print("Number of passing tests:", pass_count)

def test_sum_dwellings(housing_sale_counts):
    if (housing_sale_counts['All_dwelling_types']) == (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']):
        return True
    elif (housing_sale_counts['All_dwelling_types']) != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']):
        return False
    else:
        return np.nan
    
def test_sum_dwellings(housing_sale_counts):
    if (housing_sale_counts['All_dwelling_types']) == (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']):
        return True
    else:
        return False
    
Join = input('Would you like to join me?')
if Join.lower() == 'yes':
  print("Great," + myName + '!')
else:
  print ("Sorry for asking...")
  
  print(test_sum_dwellingss(housing_sale_counts.all()))
  
  
  def test_sum_dwellings(housing_sale_counts):
    if (housing_sale_counts.all(['All_dwelling_types'])) == (housing_sale_counts.all(['Detached']) + housing_sale_counts.all(['Semi-detached']) + housing_sale_counts.all(['Terraced']) + housing_sale_counts.all(['Flats'])):
        return True
    else:
        return Falsedef test_sum_dwellings(housing_sale_counts):
    if (housing_sale_counts.all(['All_dwelling_types'])) == (housing_sale_counts.all(['Detached']) + housing_sale_counts.all(['Semi-detached']) + housing_sale_counts.all(['Terraced']) + housing_sale_counts.all(['Flats'])):
        return True
    else:
        return False
    
pd.Series([False, False]).any()
False

Using np.count_nonzero() gives the number of True, i.e., the number of elements that satisfy the condition.
print(np.count_nonzero(a < 4))

print('Spark' in df['Courses'].unique())



pass_count = 0
for All_dwelling_types in housing_sale_counts:


    if All_dwelling_types.all() == housing_sale_counts['Detached'].all():


        pass_count += 1

c = housing_sale_counts['All_dwelling_types']
if c.any() != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']).any():
    print("Great")
else:
    print("Sorry for asking...")

def test_sum_dwellings(housing_sale_counts['All_dwelling_types'].any()):
    if housing_sale_counts['All_dwelling_types'].any() != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']).any():
        print("Fail. A fail means sum of columns do not equal total.")
        return False
    else:
        print("Pass. A pass means sum of columns equals total.")
        return True

def test_sum_dwellings():
    if housing_sale_counts['All_dwelling_types'].any() != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']).any():
        print("Fail. A fail means sum of columns do not equal total.")
        
    else:
        print("Pass. A pass means sum of columns equals total.")
        
print(test_sum_dwellings)

if housing_sale_counts['All_dwelling_types'].any() != (housing_sale_counts['Detached'] + housing_sale_counts['Semi-detached'] + housing_sale_counts['Terraced'] + housing_sale_counts['Flats']).any():
    print("Fail. A fail means sum of columns do not equal total.")
else:
    print("Pass. A pass means sum of columns equals total.")

print (test_sum_dwellings())

def function_that_prints():
    print "I printed"

def function_that_returns():
    return "I returned"

f1 = function_that_prints()
f2 = function_that_returns()
print "Now let us see what the values of f1 and f2 are"
print f1
print f2