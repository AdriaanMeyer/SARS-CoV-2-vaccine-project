import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Set the relevant column
y1_column = '2 Week Anti S Results'

# Create a box and whiskers chart for 2 Week Anti S Results
sns.boxplot(y=df[y1_column])
plt.title('Box and Whiskers Chart - 2 Week Anti S Results')
plt.ylabel('2 Week Anti S Results')
plt.show()

# Set the relevant column
y2_column = '4 Week Anti S Results'

# Create a box and whiskers chart for 4 Week Anti S Results
sns.boxplot(y=df[y2_column])
plt.title('Box and Whiskers Chart - 4 Week Anti S Results')
plt.ylabel('4 Week Anti S Results')
plt.show()

# Set the relevant column
y3_column = '8 Week Anti S Results'

# Create a box and whiskers chart for 8 Week Anti S Results
sns.boxplot(y=df[y3_column])
plt.title('Box and Whiskers Chart - 8 Week Anti S Results')
plt.ylabel('8 Week Anti S Results')
plt.show()

