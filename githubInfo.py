from github import Github


def getPublicRepositories(username):
    token = "" # if you get exception on limit request please set your personal github token 
    if(token):
        github = Github(token)
    else:
        github = Github()
    user = github.get_user(username)
    repos = []
    for repo in user.get_repos():
        repos.append(repo)
    return repos


def printTotalCountAndMean(repos):
    dic = {'commits': [], 'stars': [], 'contributors': [], 'branches': [], 'tags': [], 'forks': [], 'releases': [], 'closedIssues': [], 'environments': []}
    languages = dict()
    for repo in repos:
        print("Full name:", repo.full_name)
        dic['commits'].append(repo.get_commits().totalCount)
        dic['stars'].append(repo.stargazers_count)
        dic['contributors'].append(repo.get_contributors().totalCount)
        dic['branches'].append(repo.get_branches().totalCount)
        dic['tags'].append(repo.get_tags().totalCount)
        dic['forks'].append(repo.forks_count)
        dic['releases'].append(repo.get_releases().totalCount)
        dic['closedIssues'].append(repo.get_issues(state='closed').totalCount)
        dic['environments'].append(repo.get_workflows().totalCount)
        
        for language, codelines in repo.get_languages().items():
            if (language in list(languages.keys())):
                languages[language].append(int(codelines))
            else:
                languages[language] = [int(codelines)]

    print('-'*50)
    
    for key,value in dic.items():
        value.sort()
        mean = "{:.2f}".format(sum(value)/len(repos))
        median = (value[int(len(value)/2 - 0.5)] + value[int(len(value)/2)])/2
        print(f'{key}: all = {value}, total = {sum(value)}, mean = {mean}, median = {median}')
    
    print('-'*50)

    for language, codeLines in languages.items():
        codeLines.sort()
        mean = "{:.2f}".format(sum(codeLines)/len(repos))
        median = (codeLines[int(len(codeLines)/2 - 0.5)] + codeLines[int(len(codeLines)/2)])/2
        print(f'{language}: all = {codeLines}, total = {sum(codeLines)}, mean = {mean} , median = {median}')
    

def run(account):
    repos = getPublicRepositories(account)
    printTotalCountAndMean(repos)


if __name__ == '__main__':
    account = 'kaggle'
    run(account)