import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Plot a regression plot for 2 Week Anti S Results vs. 8 Week Anti S Results
sns.regplot(x='2 Week Anti S Results', y='8 Week Anti S Results', data=df, label='2 Week vs. 8 Week')

# Set the y-axis limits if needed
plt.ylim(0, max(df['8 Week Anti S Results']) + 1)

# Plot a regression plot for 2 Week Anti S Results vs. 4 Week Anti S Results
sns.regplot(x='2 Week Anti S Results', y='4 Week Anti S Results', data=df, label='2 Week vs. 4 Week')

# Set the y-axis limits
plt.ylim(0, max(df['4 Week Anti S Results']) + 1)

# Add legend
plt.legend()

# Show the plot
plt.show()