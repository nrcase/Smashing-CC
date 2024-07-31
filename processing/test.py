from github import Github, Auth

rate_limit = g.get_rate_limit()

# Print rate limit details
print("Rate limit details:")
print(f"Core limit: {rate_limit.core.limit}")
print(f"Core remaining: {rate_limit.core.remaining}")
print(f"Core reset: {rate_limit.core.reset}")


organization = g.get_organization("ComparativeComprehension")

repo = organization.get_repo("Code-Review-sbpatel6")

for pr in repo.get_pulls(state='all'):
    for review in pr.get_reviews():
        print(review.state)

for pr in repo.get_pulls(state='all'):
    print(pr.is_merged())
    
# for pr in repo.get_pulls(state='all'): ##prints the comments in the order from top to bottom of the PRs
#     for comment in pr.get_comments():
#         print(comment.body)
        
### if they do approved, comes back as APPROVED
### if they do changes requested, comes back as CHANGES_REQUESTED
### if they do nothing and has comments, comes back as COMMENTED
### if they do nothing and does not have comments, comes back as PENDING