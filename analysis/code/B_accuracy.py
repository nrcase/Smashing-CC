import pandas as pd

person = pd.read_csv("/Users/nrcase/research/cc-repo/cc/df/best/people_df.csv")
problem = pd.read_csv("/Users/nrcase/research/cc-repo/cc/df/best/problem_df.csv")

df = problem[problem['problem'] == 'B']
df.drop(columns=['size', 'depth', 'gpt', 'modality', 'Pttn', 'Trust', 'Exp', 'order'], inplace=True)

person.drop(columns=['AvgAcc', 'GPT', 'Modality', 'Pttn'], inplace=True)
df = df.merge(person, on='person', how='left')

df.to_csv("/Users/nrcase/research/cc-repo/cc/df/best/B_accuracy.csv", index=False)