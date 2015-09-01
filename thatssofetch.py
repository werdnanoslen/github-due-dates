from github import Github
import re

g = Github('19f95493be1225258f1a6edc2aeb62a61292eecc')

org = g.get_organization('codeforatlanta')
repos = org.get_repos()
for repo in repos:
    issues = repo.get_issues()
    for issue in issues:
        body = issue.body
        hasDueDate = body.find('#due ') > -1
        if hasDueDate:
            monthIndexStart = body.find('#due ') + 5
            monthIndexEnd = body.find('/', monthIndexStart)
            month = body[monthIndexStart:monthIndexEnd]
            day = re.search('(/)\w+', body[monthIndexEnd:]).group(0)[1:]
            print(month, day)
