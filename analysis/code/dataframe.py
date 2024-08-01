import pandas as pd
import mysql.connector

## connect to sql database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)
mycursor = mydb.cursor()
mycursor.execute("USE cc")

## import the post study and the base for the dataframe
post = pd.read_csv('/Users/nrcase/research/cc-repo/cc/statistics/post_study.csv')
df = pd.read_csv('full_dataframe.csv', header=0)

## rename the gen ai column
post.rename(columns={'For how many tasks, approximately, did you consult the following resources? [Generative AI (e.g. ChatGPT)]': 'gen'}, inplace=True)

## function to get anon name from unityID
def lookup_name(unityID):
    for line in mapping:
        if unityID in line:
            return line.split(',')[1]
        
## function to get pattern from the unityID
def lookup_pattern(unityID):
    for line in mapping:
        if unityID in line:
            return line.split(',')[2]

## function to get the gpt value from post study dataframe, searchs on username and organizes by ncsu0-ncsu-124
## first transform real into anon, and get in order list of real and then use that 
def get_gpt(username, post):
    username = username + '@ncsu.edu'
    return post.query('`Email Address` == @username')['gen'].values[0]

## get modality from post study, dataframe checks for username, will check if out of order
def get_modality(username, post):
    username = username + '@ncsu.edu'
    return post.query('`Email Address` == @username')['What kind of computing device did you use to complete this study? '].values[0]

def get_pattern_df(username, df):
    return df.query('person == @username')['Pttn'].values[0]

def get_expected(username, df, task):
        return df.query('person == @username and problem == @task')['Exp'].values[0]

## opens the mapping file
with open('/Users/nrcase/research/cc-repo/cc/processing/mapping.txt', '+r') as file:
    mapping = file.read().splitlines()
    
## creates list of anon names and real names in the right order
name_list = []
real_list = []
for name in mapping:
    real_list.append(name.split(',')[0])
    name_list.append(lookup_name(name))

## creates list of patterns in the right order, ncsu0-ncsu124
pattern_list = []
for pattern in mapping:
    pattern_list.append(lookup_pattern(pattern))

## create and put in the usernames and patterns and depths and sizes to the dataframe
repeated_usernames = [user for user in name_list for _ in range(8)]
repeated_patterns = [pattern for pattern in pattern_list for _ in range(8)]

task_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
size_list = ['small', 'small', 'large', 'large', 'small', 'small', 'large', 'large']
depth_list = ['shallow', 'shallow', 'shallow', 'shallow', 'deep', 'deep', 'deep', 'deep']

df['person'] = repeated_usernames
df['Pttn'] = repeated_patterns
df['problem'] = task_list * 125
df['size'] = size_list * 125
df['depth'] = depth_list * 125

## get the gpt values
gpt_list = []
for i in range(0, 125):
    gpt_list.append(get_gpt(real_list[i], post))
repeated_gpt = [gpt for gpt in gpt_list for _ in range(8)]
df['gpt'] = repeated_gpt

## get mode values
mode_list = []
for i in range(0, 125):
    mode_list.append(get_modality(real_list[i], post))
repeated_mode = [mode for mode in mode_list for _ in range(8)]
df['modality'] = repeated_mode

## get trust values
for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    trust_list = []
    query = "SELECT {}_trust FROM repos_manual WHERE anon = %s".format(letter)
    for i in range(0, 125):
        mycursor.execute(query, (name_list[i],))
        result = mycursor.fetchone()
        trust_list.append(int(result[0]))
    df.loc[df['problem'] == letter, 'Trust'] = trust_list

## get expected values
with open('/Users/nrcase/research/cc-repo/cc/statistics/patterns.csv', '+r') as file:
    patterns = file.read().splitlines()
    
df['Exp'] = df['Exp'].astype(str)
for anon in name_list:
    pattern_id = get_pattern_df(anon, df)
    pattern = patterns[int(pattern_id)]
    pattern = pattern.split(',')
    
    problems = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for i, problem in enumerate(problems):
        df.loc[(df['person'] == anon) & (df['problem'] == problem), 'Exp'] = str(pattern[i])

## get merge values, list is in order of ncsu0-124, A-H
merge_list = []
for i in range(0, 125):
    for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        query = "SELECT {}_merge FROM repos_manual WHERE anon = %s".format(letter)
        mycursor.execute(query, (name_list[i],))
        result = mycursor.fetchone()
        merge_list.append(int(result[0]))

##get expected values
expected_list = []
for anon in name_list:
    for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        expected_list.append(get_expected(anon, df, letter))
        
expected_list = [1 if item == 'Eq' else 0 for item in expected_list]

for i in range(0, 1000):
    if int(merge_list[i]) == int(expected_list[i]):
        df.loc[i, 'accuracy'] = 1
    else:
        df.loc[i, 'accuracy'] = 0

#print(df.head(40))
df.to_csv('full_dataframe.csv', index=False)


condition = (df['problem'] == 'D') & (df['Exp'] == 'Eq')

filtered_df = df[~condition]

filtered_df.to_csv('filtered_dataframe.csv', index=False)

