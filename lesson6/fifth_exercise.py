import pandas as pd

read_file = pd.read_excel('data_score.xlsx')
read_file.to_csv('data_score_csv_formal.csv', encoding='utf-8', index=None, header=True)
df = pd.DataFrame(pd.read_csv("data_score_csv_formal.csv"))
print(df)
