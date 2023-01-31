import pandas as pd

df = pd.DataFrame(pd.read_csv("E:\\assingment\day3\work.csv"))

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')

print('Year Month Day Hour Minute Second')
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['hour'] = df['Date'].dt.hour
df['minute'] = df['Date'].dt.minute
df['second'] = df['Date'].dt.second

print(df.head(23674))