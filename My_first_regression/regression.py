# Import numpy and pandas libraries to read the data, statsmodel to run regression and matplotlib and seaborn libraries to visualize the data
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt 
import seaborn as sns

# Read the CSV file on possum and view some data points
possum = pd.read_csv("C:\\Users\\maroos/Downloads/possum.csv")
possum

# Show the column names
possum.columns

# Read total number of rows and columns in the data
nrow, ncol = possum.shape
print("There are", nrow, "rows and", ncol, "columns in possum data frame")

# Describe dataset
possum.describe()

# Research Question: Can we use total length to predict a possum's head length?

# Use pairplot to visualize the data for correlation
sns.pairplot(possum, x_vars=['skullw','totlngth', 'taill', 'footlgth'], 
             y_vars='hdlngth', size=4, aspect=1, kind='scatter')
plt.show()

# Visualize the data using heatmap
sns.heatmap(possum.corr(), cmap="YlGnBu", annot = True)
plt.show()

# Create x and y variables
x = possum['skullw']
y = possum['hdlngth']

#add constant to predictor variables
x = sm.add_constant(x)

#fit linear regression model
model = sm.OLS(y, x).fit()

#view model summary
print(model.summary())
