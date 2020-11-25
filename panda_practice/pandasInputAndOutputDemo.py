import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('example.csv')
df.to_excel('exampleExcel.xlsx',sheet_name="Demo",index=False)

print(pd.read_excel('exampleExcel.xlsx',sheet_name='Demo'))

# data = pd.read_html("http://www.flipkart.com")
# print(type(data))

engine = create_engine('sqlite:///:memory:')
print(df.to_sql('my_table', engine))

sqldf = pd.read_sql('my_table',con=engine)
print(sqldf)
