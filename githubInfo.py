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
    dic = {'commits': 0, 'stars': 0, 'contributors': 0, 'branches': 0, 'tags': 0, 'forks': 0, 'releases': 0, 'closedIssues': 0}
    languages = dict()
    for repo in repos:
        print("Full name:", repo.full_name)
        dic['commits'] += repo.get_commits().totalCount
        dic['stars'] += repo.stargazers_count
        dic['contributors'] += repo.get_contributors().totalCount
        dic['branches'] += repo.get_branches().totalCount
        dic['tags'] += repo.get_tags().totalCount
        dic['forks'] += repo.forks_count
        dic['releases'] += repo.get_releases().totalCount
        dic['closedIssues'] += repo.get_issues(state='closed').totalCount
        
        for language, codelines in repo.get_languages().items():
            if (language in list(languages.keys())):
                languages[language] += int(codelines)
            else:
                languages[language] = int(codelines)

    print('-'*50)
    
    for key,value in dic.items():
        mean = "{:.2f}".format(value/len(repos))
        print(f'{key} : total = {value}, mean = {mean}')
    
    print('-'*50)

    for language, totalCodeLine in languages.items():
        mean = "{:.2f}".format(totalCodeLine/len(repos))
        print(f'{language} : total = {totalCodeLine}, mean = {mean}')
    

def run(account):
    repos = getPublicRepositories(account)
    printTotalCountAndMean(repos)


if __name__ == '__main__':
    account = 'kaggle'
    run(account)