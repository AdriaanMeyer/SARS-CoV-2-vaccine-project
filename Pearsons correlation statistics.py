import pandas as pd
from scipy import stats

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Calculate Pearson correlation coefficient and p-value
pearson_coef, p_value = stats.pearsonr(df['2 Week Anti S Results'], df['4 Week Anti S Results'])

print("Pearson correlation coefficient:", pearson_coef)
print("P-value:", p_value)

# Calculate Pearson correlation coefficient and p-value
pearson_coef, p_value = stats.pearsonr(df['2 Week Anti S Results'], df['8 Week Anti S Results'])

print("Pearson correlation coefficient:", pearson_coef)
print("P-value:", p_value)

# Calculate Pearson correlation coefficient and p-value
pearson_coef, p_value = stats.pearsonr(df['4 Week Anti S Results'], df['8 Week Anti S Results'])

print("Pearson correlation coefficient:", pearson_coef)
print("P-value:", p_value)
