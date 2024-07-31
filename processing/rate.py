from github import Github, Auth

rate_limit = g.get_rate_limit()

# Print rate limit details
print("Rate limit details:")
print(f"Core limit: {rate_limit.core.limit}")
print(f"Core remaining: {rate_limit.core.remaining}")
print(f"Core reset: {rate_limit.core.reset}")