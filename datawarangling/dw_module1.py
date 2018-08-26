import pandas as pd

df = pd.read_csv("titanic.csv")

print(df.head(10))
print(df.columns.values, list(df))
print(df.ticket.value_counts())
print(df.info(), df.corr())

df = df['pclass', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest', 'survived']


