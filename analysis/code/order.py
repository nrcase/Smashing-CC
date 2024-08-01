from github import Github, Auth

def get_letter_from_name(name):
    name = name.lower()
    #print(name)
    if name == 'pythag':
        return 'A'
    elif name == 'limit1':
        return 'B'
    elif  name == 'pow':
        return 'C'
    elif name == 'conflict':
        return 'D'
    elif name == 'sign':
        return 'E'
    elif name == 'optimization':
        return 'F'
    elif name == 'tcas':
        return 'G'
    elif name == 'ejhash':
        return 'H'
    else:
        #print(name)
        return 'ERROR'

access_token = ""
auth = Auth.Token(access_token)
g = Github(base_url="https://github.ncsu.edu/api/v3", auth=auth)

with open("/Users/nrcase/research/cc-repo/cc/processing/modified_mapping.txt", "r") as file: #use modified_mapping when ready to go
   lines = file.read().splitlines()
   
organization = g.get_organization("ComparativeComprehension")

class Order:
    def __init__(self, name, A, B, C, D, E, F, G, H):
        self.name = name
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.G = G
        self.H = H
    
    def __str__(self):
        return self.name + "," + str(self.A) + "," + str(self.B) + "," + str(self.C) + "," + str(self.D) + "," + str(self.E) + "," + str(self.F) + "," + str(self.G) + "," + str(self.H)
    
    def assign_places(self,letter, num):
        if letter == 'A':
            self.A = num
        elif letter == 'B':
            self.B = num
        elif letter == 'C':
            self.C = num
        elif letter == 'D':
            self.D = num
        elif letter == 'E':
            self.E = num
        elif letter == 'F':
            self.F = num
        elif letter == 'G':
            self.G = num
        elif letter == 'H':
            self.H = num
        else:
            print("ERROR")
            return

for id in lines:
    ## get the real and anon id
    array = id.split(",")
    real = array[0]
    anon = array[1]
    print(real)
    
    repo = organization.get_repo("Code-Review-" + real)
    ## for each pr in the repo
    o = Order(anon, 0, 0, 0, 0, 0, 0, 0, 0)
    count = 8
    for pr in repo.get_pulls(state='all'):
        current_pr = pr.title
        letter = get_letter_from_name(current_pr.split(" ")[0])
        o.assign_places(letter,count)
        count -= 1
    
    with open("/Users/nrcase/research/cc-repo/cc/processing/order.txt", "a") as file:
        file.write(str(o) + "\n")
        

   

   
