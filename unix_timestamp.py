import pandas as pd

df = pd.DataFrame(pd.read_csv("E:\\assingment\day3\work.csv"))

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
print(df)

for i in df['Date']:
    n = int(i.value/1000000000)
    print(n, end="\n")   