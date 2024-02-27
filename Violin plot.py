import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Set the relevant columns
x_column = 'Gender'
y_column = '2 Week Anti S Results'

# Create a violin plot
sns.violinplot(x=x_column, y=y_column, data=df, palette='muted')
plt.title('Violin Plot - 2 Week Anti S Results by Gender')
plt.xlabel('Gender')
plt.ylabel('2 Week Anti S Results')
plt.show()
