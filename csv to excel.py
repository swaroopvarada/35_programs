import pandas as pd
df = pd.read_csv("E:\\assingment\day3\work.csv")
df.to_excel ('E:/newwork.xlsx', index = None, header=True)
print('done')