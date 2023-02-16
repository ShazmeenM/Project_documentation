# Import numpy and pandas libraries to read the data, statsmodel to run regression and matplotlib and seaborn libraries to visualize the data
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt 
import seaborn as sns
import datetime
import yaml
from quarto import render


out_filename = "regression_QA_test"


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
print(model.rsquared)

def tss(x):
    return ((x - np.mean(x))**2).sum()

print(tss(x))

# Calculating the value of r-squared to get it printed in the qmd report

def __init__(self, theta_0, theta_1):

    self.theta_0 = theta_0
    self.theta_1 = theta_1
    self.r_squared = None
    self.residuals = None

@property
def theta_0(self):
    return self._theta_0

@theta_0.setter
def theta_0(self, value):
    if not isinstance(value, (int, float)):
        raise TypeError("theta_0 must be an int or float")
    self._theta_0 = value
        
        
@property
def theta_1(self):
    return self._theta_1

@theta_1.setter
def theta_1(self, value):
    if not isinstance(value, (int, float)):
        raise TypeError("theta_1 must be an int or float")
    self._theta_1 = value

def calculate_predicted_values(self, x):
    """
    Calculates predicted values of the dependent variable, y, according to the
    straight-line equation y = mx + c for given x, m (theta_1) and c(theta_0),
    where x is an array of values
    Parameters
    -------
    x : Training data (array-like of floats)
    theta_0 : y-intercept of the model (float)
    theta_1 : gradient of the model (float)
    Returns
    -------
    y_predicted : The predicted y-values at each point x (array of floats)
    """
    y_predicted = (self.theta_1 * x) + self.theta_0

    return y_predicted

def calculate_residuals_array(self, x, y):
    """
    Calculates the difference between predicted y-values (from the
    hypothesis function) and the actual y-values from the dataset.
    Parameters
    -------
    x : Training data (array-like of floats)
    y : The target/actual y-values at each point x (array-like of floats)
    Returns
    -------
    residuals_array : Residuals, i.e. the difference between predicted and 
    actual y-values (array of floats)
    """
    residuals_array = np.subtract(self.calculate_predicted_values(x), np.asarray(y))
    self.residuals = residuals_array

    return residuals_array

# Calculate the residual sum of squares
def calculate_RSS(self, residuals_array):
    residual_squared = np.square(residuals_array)
    residual_sum_squares = sum(residual_squared)
    
    return residual_sum_squares

# Calculate the total sum of squares
def  calculate_TSS(self, y):
    y_mean = np.mean(y)
    y_diff = y - y_mean
    total_sum_squares = sum(np.square(y_diff))
    
    return total_sum_squares

# Calculate the co-efficient of determination of the model (r-squared)

def calculate_r_squared(self, RSS, TSS):
    r_squared = 1 - (RSS / TSS)
    
    return r_squared

r_squared = calculate_r_squared

render(
    input = "report.qmd", 
    output_format = "html",
    output_file = out_filename, 
    execute_params = {
        "r_squared" : print(model.rsquared)
    }
    )
