import pandas as pd

## function to get anon name from unityID
def lookup_name(unityID):
    for line in mapping:
        if unityID in line:
            return line.split(',')[1]
        
## opens the mapping file
with open('/Users/nrcase/research/cc-repo/cc/processing/files/fixed_mapping.txt', '+r') as file:
    mapping = file.read().splitlines()

df = pd.read_csv('/Users/nrcase/research/cc-repo/cc/df/best/people_df.csv')

section1 = pd.read_csv('/Users/nrcase/research/cc-repo/cc/statistics/files/section1.csv')

section2 = pd.read_csv('/Users/nrcase/research/cc-repo/cc/statistics/files/section2.csv')

section1_name = section1['Email Address']
cleaned_list_1 = [email.replace('@ncsu.edu', '') for email in section1_name]

section_2_name = section2['Email Address']
cleaned_list_2 = [email.replace('@ncsu.edu', '') for email in section_2_name]

anon_1 = []
for name in cleaned_list_1:
    anon_1.append(lookup_name(name))
    
anon_2 = []
for name in cleaned_list_2:
    anon_2.append(lookup_name(name))
    
print(len(anon_1))
print(len(anon_2))

print(anon_1)
#print(anon_2)

done_1 = df[df['person'].isin(anon_1)]
done_2 = df[df['person'].isin(anon_2)]


done_1.to_csv('/Users/nrcase/research/cc-repo/cc/df/best/section1.csv')
done_2.to_csv('/Users/nrcase/research/cc-repo/cc/df/best/section2.csv')











