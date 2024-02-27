import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Extract relevant columns from DataFrame
x_column = 'Staff Number'
y_column = '2 Week Anti S Results'

# Seaborn horizontal barplot
sns.barplot(x=x_column, y=y_column, data=df, orient='v')

# Matplotlib customization
plt.title('2-Week post-booster Bar Chart')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.show()

