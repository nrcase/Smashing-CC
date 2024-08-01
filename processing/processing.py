from github import Github, Auth
import mysql.connector

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
    
# to be trusted for equivlenent, you must have merged, approved and not requested changes, comments are optional
def check_trust_Eq(merge, comment, approve, request):
    if merge == True and approve == True and request == False:
        return True
    else:
        return False

# to be trusted for not equivalent, you must have not merged, had comments and then requested changes
def check_trust_Neq(merge, comment, approve, request):
    if merge == False and comment == True and approve == False and request == True:
        return True
    else:
        return False

rate_limit = g.get_rate_limit()

# Print rate limit details
print("Rate limit details:")
print(f"Core limit: {rate_limit.core.limit}")
print(f"Core remaining: {rate_limit.core.remaining}")
print(f"Core reset: {rate_limit.core.reset}")


organization = g.get_organization("ComparativeComprehension")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)
mycursor = mydb.cursor()

with open("/Users/nrcase/research/cc-repo/cc/processing/modified_mapping.txt", "r") as file: #use modified_mapping when ready to go
   lines = file.read().splitlines()
   
mycursor.execute("USE cc")

for id in lines:
    
    A_merge = A_comment = A_approve = A_request = A_trust = A_link = \
    B_merge = B_comment = B_approve = B_request = B_trust = B_link = \
    C_merge = C_comment = C_approve = C_request = C_trust = C_link = \
    D_merge = D_comment = D_approve = D_request = D_trust = D_link = \
    E_merge = E_comment = E_approve = E_request = E_trust = E_link = \
    F_merge = F_comment = F_approve = F_request = F_trust = F_link = \
    G_merge = G_comment = G_approve = G_request = G_trust = G_link = \
    H_merge = H_comment = H_approve = H_request = H_trust = H_link = False
    
    ## get the real and anon id
    array = id.split(",")
    real = array[0]
    anon = array[1]
    print(anon)
    
    ## get the repo
    repo = organization.get_repo("Code-Review-" + real)
    
    ## for each pr in the repo
    for pr in repo.get_pulls(state='all'):
        # convert title to letter
        current_pr = pr.title
        letter = get_letter_from_name(current_pr.split(" ")[0])
        #print(pr)
        # print(letter)
        # if letter == 'ERROR':
        #     print(current_pr)
        #     print(real)
        
        # check the merge state of the pr
        if letter == 'A' and pr.is_merged():
            A_merge = True
        elif letter == 'B' and pr.is_merged():
            B_merge = True
        elif letter == 'C' and pr.is_merged():
            C_merge = True
        elif letter == 'D' and pr.is_merged():
            D_merge = True
        elif letter == 'E' and pr.is_merged():
            E_merge = True
        elif letter == 'F' and pr.is_merged():
            F_merge = True
        elif letter == 'G' and pr.is_merged():
            G_merge = True
        elif letter == 'H' and pr.is_merged():
            H_merge = True
            
        # check for review comments, comments made against the diff
        if letter == 'A' and pr.get_review_comments().totalCount > 0:
            A_comment = True
        elif letter == 'B' and pr.get_review_comments().totalCount > 0:
            B_comment = True
        elif letter == 'C' and pr.get_review_comments().totalCount > 0:
            C_comment = True
        elif letter == 'D' and pr.get_review_comments().totalCount > 0:
            D_comment = True
        elif letter == 'E' and pr.get_review_comments().totalCount > 0:
            E_comment = True
        elif letter == 'F' and pr.get_review_comments().totalCount > 0:
            F_comment = True
        elif letter == 'G' and pr.get_review_comments().totalCount > 0:
            G_comment = True
        elif letter == 'H' and pr.get_review_comments().totalCount > 0:
            H_comment = True

        ## checks for highest level PR comments
        if letter == 'A' and pr.get_issue_comments().totalCount > 0:
            A_comment = True
        elif letter == 'B' and pr.get_issue_comments().totalCount > 0:
            B_comment = True
        elif letter == 'C' and pr.get_issue_comments().totalCount > 0:
            C_comment = True
        elif letter == 'D' and pr.get_issue_comments().totalCount > 0:
            D_comment = True
        elif letter == 'E' and pr.get_issue_comments().totalCount > 0:
            E_comment = True
        elif letter == 'F' and pr.get_issue_comments().totalCount > 0:
            F_comment = True
        elif letter == 'G' and pr.get_issue_comments().totalCount > 0:
            G_comment = True
        elif letter == 'H' and pr.get_issue_comments().totalCount > 0:
            H_comment = True
            
        ## some people didn't do in line comments, but need just comments when doing review so here
        for review in pr.get_reviews():
            if letter == 'A' and review.body.__len__() > 0:
                A_comment = True
            elif letter == 'B' and review.body.__len__() > 0:
                B_comment = True
            elif letter == 'C' and review.body.__len__() > 0:
                C_comment = True
            elif letter == 'D' and review.body.__len__() > 0:
                D_comment = True
            elif letter == 'E' and review.body.__len__() > 0:
                E_comment = True
            elif letter == 'F' and review.body.__len__() > 0:
                F_comment = True
            elif letter == 'G' and review.body.__len__() > 0:
                G_comment = True
            elif letter == 'H' and review.body.__len__() > 0:
                H_comment = True
            
        # check for approval
        for review in pr.get_reviews():
            if letter == 'A' and review.state == 'APPROVED':
                A_approve = True
            elif letter == 'B' and review.state == 'APPROVED':
                B_approve = True
            elif letter == 'C' and review.state == 'APPROVED':
                C_approve = True
            elif letter == 'D' and review.state == 'APPROVED':
                D_approve = True
            elif letter == 'E' and review.state == 'APPROVED':
                E_approve = True
            elif letter == 'F' and review.state == 'APPROVED':
                F_approve = True
            elif letter == 'G' and review.state == 'APPROVED':
                G_approve = True
            elif letter == 'H' and review.state == 'APPROVED':
                H_approve = True
        
        # check for request changes
        for review in pr.get_reviews():
            if letter == 'A' and review.state == 'CHANGES_REQUESTED':
                A_request = True
            elif letter == 'B' and review.state == 'CHANGES_REQUESTED':
                B_request = True
            elif letter == 'C' and review.state == 'CHANGES_REQUESTED':
                C_request = True
            elif letter == 'D' and review.state == 'CHANGES_REQUESTED':
                D_request = True
            elif letter == 'E' and review.state == 'CHANGES_REQUESTED':
                E_request = True
            elif letter == 'F' and review.state == 'CHANGES_REQUESTED':
                F_request = True
            elif letter == 'G' and review.state == 'CHANGES_REQUESTED':
                G_request = True
            elif letter == 'H' and review.state == 'CHANGES_REQUESTED':
                H_request = True
        
        # check for trust
        
        if letter == 'A' and (check_trust_Eq(A_merge, A_comment, A_approve, A_request) or check_trust_Neq(A_merge, A_comment, A_approve, A_request)):
            A_trust = True
        elif letter == 'B' and (check_trust_Eq(B_merge, B_comment, B_approve, B_request) or check_trust_Neq(B_merge, B_comment, B_approve, B_request)):
            B_trust = True
        elif letter == 'C' and (check_trust_Eq(C_merge, C_comment, C_approve, C_request) or check_trust_Neq(C_merge, C_comment, C_approve, C_request)):
            C_trust = True
        elif letter == 'D' and (check_trust_Eq(D_merge, D_comment, D_approve, D_request) or check_trust_Neq(D_merge, D_comment, D_approve, D_request)):
            D_trust = True
        elif letter == 'E' and (check_trust_Eq(E_merge, E_comment, E_approve, E_request) or check_trust_Neq(E_merge, E_comment, E_approve, E_request)):
            E_trust = True
        elif letter == 'F' and (check_trust_Eq(F_merge, F_comment, F_approve, F_request) or check_trust_Neq(F_merge, F_comment, F_approve, F_request)):
            F_trust = True
        elif letter == 'G' and (check_trust_Eq(G_merge, G_comment, G_approve, G_request) or check_trust_Neq(G_merge, G_comment, G_approve, G_request)):
            G_trust = True
        elif letter == 'H' and (check_trust_Eq(H_merge, H_comment, H_approve, H_request) or check_trust_Neq(H_merge, H_comment, H_approve, H_request)):
            H_trust = True
        
        # get link
        if letter == 'A':
            A_link = pr.html_url
        elif letter == 'B':
            B_link = pr.html_url
        elif letter == 'C':
            C_link = pr.html_url
        elif letter == 'D':
            D_link = pr.html_url
        elif letter == 'E':
            E_link = pr.html_url
        elif letter == 'F':
            F_link = pr.html_url
        elif letter == 'G':
            G_link = pr.html_url
        elif letter == 'H':
            H_link = pr.html_url
    
    # insert into the database
    mycursor.execute("""
    UPDATE repos 
    SET 
    A_merge = %s, A_comment = %s, A_approve = %s, A_request = %s, A_trust = %s, A_link = %s, 
    B_merge = %s, B_comment = %s, B_approve = %s, B_request = %s, B_trust = %s, B_link = %s, 
    C_merge = %s, C_comment = %s, C_approve = %s, C_request = %s, C_trust = %s, C_link = %s, 
    D_merge = %s, D_comment = %s, D_approve = %s, D_request = %s, D_trust = %s, D_link = %s, 
    E_merge = %s, E_comment = %s, E_approve = %s, E_request = %s, E_trust = %s, E_link = %s, 
    F_merge = %s, F_comment = %s, F_approve = %s, F_request = %s, F_trust = %s, F_link = %s, 
    G_merge = %s, G_comment = %s, G_approve = %s, G_request = %s, G_trust = %s, G_link = %s, 
    H_merge = %s, H_comment = %s, H_approve = %s, H_request = %s, H_trust = %s, H_link = %s
    WHERE 
    anon = %s
    """, (A_merge, A_comment, A_approve, A_request, A_trust, A_link, B_merge, B_comment, B_approve, B_request, B_trust, B_link, C_merge, C_comment, C_approve, C_request, C_trust, C_link, D_merge, D_comment, D_approve, D_request, D_trust, D_link, E_merge, E_comment, E_approve, E_request, E_trust, E_link, F_merge, F_comment, F_approve, F_request, F_trust, F_link, G_merge, G_comment, G_approve, G_request, G_trust, G_link, H_merge, H_comment, H_approve, H_request, H_trust, H_link, anon))
    mydb.commit()
            
        
        
    # print(A_merge, B_merge, C_merge, D_merge, E_merge, F_merge, G_merge, H_merge, "\n")
    # print(A_comment, B_comment, C_comment, D_comment, E_comment, F_comment, G_comment, H_comment, "\n")
    # print(A_approve, B_approve, C_approve, D_approve, E_approve, F_approve, G_approve, H_approve, "\n")
    # print(A_request, B_request, C_request, D_request, E_request, F_request, G_request, H_request, "\n")
    # print(A_trust, B_trust, C_trust, D_trust, E_trust, F_trust, G_trust, H_trust, "\n")
    # print(A_link, B_link, C_link, D_link, E_link, F_link, G_link, H_link, "\n")
    # print("-------------------\n")