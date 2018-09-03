import pandas as pd

df = pd.read_csv("titanic.csv")

print(df.head(10))
print(df.columns.values, list(df))
print(df.ticket.value_counts())
print(df.info(), df.corr())

"""
Printing the details for df update.
 df = df['pclass', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 
 'cabin', 'embarked', 'boat', 'body', 'home.dest', 'survived']
"""
import sys

from kaggle.api import kaggle_api
from kaggle import cli

sys.argv = 'kaggle competitions download -c kddbr-2018'.split()
cli.main()

kapi = kaggle_api.ApiClient()
rc = kapi.request(method="GET", url='https://www.kaggle.com/account/login')
headers = {"Content-Type": "json"}
rc1 = kapi.request(method="POST", url="https://www.kaggle.com/c/titanic/download/train.csv",
                   headers=headers)
print(rc1)
print(rc)

# thread = kapi.
#     # competitions_data_download_file(id, file_name, async_req=True)
# >>> result = thread.get()
