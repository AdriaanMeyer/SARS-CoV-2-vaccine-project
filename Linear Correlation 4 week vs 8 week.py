import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Plot a regression plot for 4 Week Anti S Results vs. 8 Week Anti S Results
sns.regplot(x='4 Week Anti S Results', y='8 Week Anti S Results', data=df,)

# Set the y-axis limits if needed
plt.ylim(0, max(df['8 Week Anti S Results']) + 1)

plt.show()