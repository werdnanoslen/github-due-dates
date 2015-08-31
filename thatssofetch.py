from github import Github

g = Github()

org = g.get_organization('')
repos = org.get_repos()

for repo in repos:
    issues = repo.get_issues()
    for issue in issues:
        print(issue.body)
