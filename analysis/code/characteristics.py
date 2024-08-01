import pandas as pd

class Person:
    def __init__(self, anon, real, ProgExp, Compared, OO, Years, Total, accuracy, GPT, Modality, Pttn):
        self.anon = anon
        self.real = real
        self.ProgExp = ProgExp
        self.Compared = Compared
        self.OO = OO
        self.Years = Years
        self.Total = Total
        self.accuracy = accuracy
        self.GPT = GPT
        self.Modality = Modality
        self.Pttn = Pttn
    
    def __str__(self):
        return f"Person(anon={self.anon}, real={self.real}, ProgExp={self.ProgExp}, Compared={self.Compared}, OO={self.OO}, Years={self.Years}, Total={self.Total}, Acc={self.accuracy})"

## function to get anon name from unityID
def lookup_name(unityID):
    for line in mapping:
        if unityID in line:
            return line.split(',')[1]
        
def get_real(line):
    return line.split(',')[0]

df = pd.read_csv('/Users/nrcase/research/cc-repo/cc/df/best/problem_df.csv')
study = pd.read_csv('/Users/nrcase/research/cc-repo/cc/statistics/files/post_study.csv')

study.rename(columns={
    "On a scale from 1 to 10, how do you estimate your programming experience? ": "Programming Experience",
    "On a scale from 1 to 10, how do you estimate your programming experience compared to your class mates?": "Compared",
    "On a scale from 1 to 5, how experienced are you with the following programming paradigm: object-oriented?": "OO",
    "Rounded to the closest integer, for how many years have you been programming?": "Years",
}, inplace=True)

## opens the mapping file
with open('/Users/nrcase/research/cc-repo/cc/processing/files/fixed_mapping.txt', '+r') as file:
    mapping = file.read().splitlines()
    
## creates list of anon names and real names in the right order
person_list = []
for name in mapping:
    person_list.append(Person(lookup_name(name), get_real(name), 0, 0, 0, 0, 0, 0,0,0,0))
    
    #max score is 35

for person in person_list:
    email = person.real + '@ncsu.edu'
    person.ProgExp = study.query('`Email Address` == @email')['Programming Experience'].values[0]
    person.Compared = study.query('`Email Address` == @email')['Compared'].values[0]
    person.OO = study.query('`Email Address` == @email')['OO'].values[0]
    person.Years = study.query('`Email Address` == @email')['Years'].values[0]
    person.Total = (person.ProgExp + person.Compared + person.OO + person.Years) / 35
    person.GPT = df.query('person == @person.anon')['gpt'].values[0]
    person.Modality = df.query('person == @person.anon')['modality'].values[0]
    person.accuracy = df.query('person == @person.anon')['accuracy'].mean()
    person.Pttn = df.query('person == @person.anon')['Pttn'].values[0]

data = []

for person in person_list:
    data.append({'person': person.anon, 'AvgAcc': person.accuracy, 'ProgExp': person.ProgExp, 'Compared': person.Compared, 'OO': person.OO, 'Years': person.Years, 'Total': person.Total, 'GPT': person.GPT, 'Modality': person.Modality, 'Pttn': person.Pttn})

new = pd.DataFrame(data)

new.to_csv('/Users/nrcase/research/cc-repo/cc/df/best/characteristics.csv', index=False)

    

    
