import pandas as pd

df = pd.read_csv('/Users/nrcase/research/cc-repo/cc/df/best/problem_full_df.csv')
condition = (df['problem'] == 'D')

filtered_df = df[~condition]

filtered_df.to_csv('problem_df.csv', index=False)