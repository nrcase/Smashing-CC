from github import Github, Auth

access_token = ""
auth = Auth.Token(access_token)
g = Github(base_url="https://github.ncsu.edu/api/v3", auth=auth)


with open("/Users/nrcase/research/cc-repo/cc/processing/modified_mapping.txt", "r") as file: #use modified_mapping when ready to go
   lines = file.read().splitlines()
   
organization = g.get_organization("ComparativeComprehension")

for id in lines:
## get the real and anon id
    array = id.split(",")
    real = array[0]
    anon = array[1]
    
    ## get the repo
    repo = organization.get_repo("Code-Review-" + real)
    
    ## for each pr in the repo
    for pr in repo.get_pulls(state='all'):
        # check if pr is open
        if pr.state == 'open':
            print(anon)
            print(pr.html_url + "\n")
            
