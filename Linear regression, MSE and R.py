import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Create a linear regression model
lm = LinearRegression()

# Define the independent variable (X) and dependent variable (Y)
X = df[["2 Week Anti S Results"]]
Y = df["4 Week Anti S Results"]

# Fit the model
lm.fit(X, Y)

# Predict Y values based on the model
yhat = lm.predict(X)

# Print the coefficients
print("Intercept (b0):", lm.intercept_)
print("Slope (b1):", lm.coef_[0])

# Create a linear regression model
lm = LinearRegression()

# Define the independent variable (X) and dependent variable (Y)
X = df[["2 Week Anti S Results"]]
Y = df["8 Week Anti S Results"]

# Fit the model
lm.fit(X, Y)

# Predict Y values based on the model
yhat = lm.predict(X)

# Print the coefficients
print("Intercept (b0):", lm.intercept_)
print("Slope (b1):", lm.coef_[0])

# Create a linear regression model
lm = LinearRegression()

# Define the independent variable (X) and dependent variable (Y)
X = df[["4 Week Anti S Results"]]
Y = df["8 Week Anti S Results"]

# Fit the model
lm.fit(X, Y)

# Predict Y values based on the model
yhat = lm.predict(X)

# Print the coefficients
print("Intercept (b0):", lm.intercept_)
print("Slope (b1):", lm.coef_[0])