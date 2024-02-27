import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Extract relevant columns from DataFrame
x_column = 'Age'

# Seaborn countplot
sns.histplot(x=x_column, data=df)

# Matplotlib customization
plt.title('Counts per age', fontsize=22)
plt.xlabel(x_column)
plt.ylabel('Count')
plt.show()

