import pandas as pd

study = pd.read_csv('/Users/nrcase/research/cc-repo/cc/statistics/files/post_study.csv')

study.rename(columns={
    'What was difficult about performing the code review in this study?': 'Difficulties',
    'What was easy about performing the code review in this study?': 'Easiness',
    'What would have helped you perform the code review in this study more effectively?': 'Effectiveness',
}, inplace=True)

with open("/Users/nrcase/research/cc-repo/cc/processing/files/mapping.txt", "r") as file: 
   lines = file.read().splitlines()
   
easy_list = []
hard_list = []
eff_list = []
anon_list = []
for id in lines:
    ## get the real and anon id
    array = id.split(",")
    real = array[0]
    anon = array[1]
    email = real + '@ncsu.edu'
    anon_list.append(anon)
    easy_list.append(study.query('`Email Address` == @email')['Easiness'].values[0])
    hard_list.append(study.query('`Email Address` == @email')['Difficulties'].values[0])
    eff_list.append(study.query('`Email Address` == @email')['Effectiveness'].values[0])

df = pd.DataFrame()
df['anon'] = anon_list
df['Easiness'] = easy_list
df['Difficulties'] = hard_list
df['Effectiveness'] = eff_list

df.to_csv('card_sort.csv', index=False, sep='#')
    