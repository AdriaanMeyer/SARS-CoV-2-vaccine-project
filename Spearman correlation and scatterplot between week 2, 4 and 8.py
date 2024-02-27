import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Select columns for correlation analysis
columns_of_interest = ['2 Week Anti S Results', '4 Week Anti S Results', '8 Week Anti S Results']

# Create a DataFrame with the selected columns
selected_columns_df = df[columns_of_interest]

# Calculate Spearman correlation matrix
spearman_corr_matrix = selected_columns_df.corr(method='spearman')

# Create a scatterplot matrix
sns.set(style="ticks")
scatterplot_matrix = sns.pairplot(selected_columns_df, kind='scatter')

# Add Spearman correlation values to the scatterplot matrix
for i, j in zip(*plt.np.triu_indices_from(scatterplot_matrix.axes, 1)):
    scatterplot_matrix.axes[i, j].annotate(f"Spearman = {spearman_corr_matrix.iloc[i, j]:.2f}",
                                           (0.5, 0.9),
                                           xycoords='axes fraction',
                                           ha='center',
                                           va='center',
                                           bbox=dict(boxstyle="round,pad=0.3", edgecolor="w", facecolor="w"))

plt.show()
