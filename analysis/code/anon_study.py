import pandas as pd

def lookup(unityID):
    for line in mapping:
        if unityID in line:
            return line.split(',')[1]

df = pd.read_csv('/Users/nrcase/research/cc-repo/cc/statistics/files/post_study.csv')

with open('/Users/nrcase/research/cc-repo/cc/processing/files/fixed_mapping.txt', '+r') as file:
    mapping = file.read().splitlines()

real = df['Email Address'].tolist()

for i in range(len(real)):
    real[i] = real[i].replace('@ncsu.edu', '')
    real[i] = lookup(real[i])
    
df.rename(columns={'Email Address': 'Anon'}, inplace=True)
    
df['Anon'] = real

df.to_csv('/Users/nrcase/research/cc-repo/cc/statistics/files/post_study_anon.csv')

