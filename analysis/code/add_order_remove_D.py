import pandas as pd

with open("/Users/nrcase/research/cc-repo/cc/processing/order.txt") as f:
    lines = f.readlines()
    
list = [line.strip().split(',') for line in lines]
cleaned_data = [[item for item in sublist if not item.startswith('ncsu')] for sublist in list]
done = [item for sublist in cleaned_data for item in sublist]

df = pd.read_csv("/Users/nrcase/research/cc-repo/cc/full_dataframe.csv", index_col=0)

df = df.assign(order=done)
df.to_csv("/Users/nrcase/research/cc-repo/cc/done2_dataframe.csv")


