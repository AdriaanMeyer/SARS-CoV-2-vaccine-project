import pandas as pd

# Load data from CSV with semicolon as separator
csv_file_path = '/Users/adriaanmeyer/Documents/GitHub/SARS-CoV-2-vaccine-project/Example 1.csv'
df = pd.read_csv(csv_file_path, sep=';')

# Display basic statistics for a specific numeric column ('2 Week Anti S Results')
specific_column_stats_2_week = df['2 Week Anti S Results'].describe()

# Display basic statistics for a specific numeric column ('4 Week Anti S Results')
specific_column_stats_4_week = df['4 Week Anti S Results'].describe()

# Display basic statistics for a specific numeric column ('8 Week Anti S Results')
specific_column_stats_8_week = df['8 Week Anti S Results'].describe()

print("\nStatistics for '2 Week Anti S Results':")
print(specific_column_stats_2_week)

print("\nStatistics for '4 Week Anti S Results':")
print(specific_column_stats_4_week)

print("\nStatistics for '8 Week Anti S Results':")
print(specific_column_stats_8_week)

