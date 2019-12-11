# This finds the best fit severities for a model using linear regression

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Read the danger/severity file for the current model
df = pd.read_csv("dangers_model_5.csv")

# Define independent and dependent variables
X = df[["Danger"]]
Y = df.drop(columns=['Danger'])
# Change variables from dataframe to arrays (either is acceptable...)
x = np.array(X)
y = np.array(Y)

# Perform linear regression to find best fit
reg = linear_model.LinearRegression()
reg.fit(x,Y)

# Print Coefficients and record data to compare against other models
print('Coefficients: \n', reg.coef_)
