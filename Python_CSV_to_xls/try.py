import pandas as pd

CSV_FILE_PATH = '/Users/leemiles/Downloads/data.csv'
df = pd.read_csv(CSV_FILE_PATH)
print(df.head(5))