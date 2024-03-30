import numpy as np

# df = pd.read_csv('pokemon_data.csv')

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df.head(5))

df = np.loadtxt('pokemon_data.txt',dtype=str,delimiter='\t')

print(df)