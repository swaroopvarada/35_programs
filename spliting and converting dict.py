import pandas as pd
df = pd.read_csv("E:\\assingment\day3\work.csv", header=None)

# Converting this DataFrame into list of dictionary
l = df.to_dict('records')

# Display result
print("Converted Dictionary:\n",l)

#spliting string

for i in l:  
    print(list(i[1]), end=",")