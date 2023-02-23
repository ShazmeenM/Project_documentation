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







## Summary of tests performed

```{python}
# Read total number of rows and columns in the data
nrow, ncol = housing_sale_counts.shape
```

```{python}
display(Markdown(f""" There are {nrow} rows and {ncol} columns in the dataset. We have performed "n" tests on the data. The data has passed "n" tests and failed "n".  """))
``` 

## Data cleaning tests  


## Table 1: List of tests (Test_number, Description, Long_description, Status, Status_description)  


## List of failed tests with their location  

Test 1:

```{python}
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
```

Test 2: Flats should be lesser than all other dwelling types  

```{python}
def test_num_flats():
    print("Description: Checks if values of a variable are always less than other.")  
    print("Data specific description: Checks if the number of flats are lesser than the number of all other dwelling types in all councils.")  
    if all(housing_sale_counts['Detached' or 'Semi-detached' or 'Terraced']) > all(housing_sale_counts['Flats']): 
        print("Status: Pass. A pass means number of flats are less than all other dwelling types in all councils.")
        return True
    else:
        print("Status: Fail. A fail means number of flats are not less than all other dwelling types in atleast one council.")
        return False
print (test_num_flats())
```

Test 3: 
Description: Checks if any of the variables in the dataset has a negative value.
Data specific description: Checks if the data on sales of detahced, semi-detached, terraced and flats has a negative value. 
```{python}
test_neg = ((housing_sale_counts['Detached' or 'Semi-detached' or 'Terraced' or 'Flats']) < 0).any()
print ("Status:")
print (test_neg)
print("Status description: A true means there is a negative values (Fail). A false means there is no negative value (Pass).")
```


Test 4: 
Description: Checks if any of the variables in the dataset has a negative value.
Data specific description: Checks if the data on prices of detahced, semi-detached, terraced and flats has a negative value. 
```{python}
test_neg = ((housing_median_sale_price['Detached' or 'Semi-detached' or 'Terraced' or 'Flats']) < 0).any()
print ("Status:")
print (test_neg)
print("Status description: A true means there is a negative values (Fail). A false means there is no negative value (Pass).")
```

Test 5: There shouldn’t be an alphabet in sales  
```{python}
```

Test 6: There shouldn’t be an alphabet in prices  
```{python}
```

Test 7a: Are there any missing values?  
Test 7b: If yes, how many?
```{python}
```

Test 8: A local authority name should only appear 5 times in data  
```{python}
```

Test 9:	A local authority code should only appear 5 times in data  
```{python}
```
Test 10: Detect outliers  
```{python}
```

How I want it like: 
Test 1: 
Description: Checks if sum of columns equals total. 
Long_description: Checks if sum of detahced, semi-detached, terraced and flats equals all dwelling types.
Status: Pass/Fail
Status_description: A pass means sum of columns equals total. A fail means sum of columns do not equals total.
If fail, location of failure: 
``` 

Failed: Error in observation 10

Test 2: Flats should be lesser than all other dwelling types  
Failed: Error ...

Test 3: There shouldn’t be a negative value in sales  
Passed 

Test 4: There shouldn’t be a negative value in prices  
Passed:

Test 5: There shouldn’t be an alphabet in sales  


Test 6: There shouldn’t be an alphabet in prices  

Test 7a: Are there any missing values?  
Test 7b: If yes, how many?

Test 8: A local authority name should only appear 5 times in data  


Test 9:	A local authority code should only appear 5 times in data  

Test 10: Detect outliers  

## Checking characteristics of the data

Test 1: Plot trend of sales and prices by dwelling types

Test 2: What does the data distribution look like? 

Test 3: Is there any correlation between tpe of dwellings and house price?

print(housing_sale_counts['Detached'].isnumeric())
a = housing_sale_counts['Detached']
a.str.isalnum()

housing_sale_counts['Detached'].astype(str).str.isnumeric()
housing_sale_counts['Semi-detached'].astype(str).str.isnumeric()
housing_sale_counts['Terraced'].astype(str).str.isnumeric()
housing_sale_counts['Flats'].astype(str).str.isnumeric()



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




