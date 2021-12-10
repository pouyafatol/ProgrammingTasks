import requests
from pprint import pprint
import base64
from github import Github
import pickle


def showUserInfo(username):
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    pprint(user_data)

def getPublicRepositories(username):
    # git = Github()
    # user = git.get_user(username)
    # with open('user.pkl','wb') as f:
    #     pickle.dump(user,f)
    with open('user.pkl','rb') as f:
        user = pickle.load(f)
    repos = []
    for repo in user.get_repos():
        repos.append(repo)
    return repos

def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    print("Language:", repo.get_languages())
    print("Number of forks:", repo.forks_count)
    print("Number of stars:", repo.stargazers_count)
    print("Number of branches:", repo.get_branches().totalCount)
    print("Number of commits:", repo.get_commits().totalCount)
    print("Number of releases:", repo.get_releases().totalCount)
    print("Number of closed issues:", repo.get_issues(state='closed').totalCount)
    print("Number of tags:", repo.get_tags().totalCount)
    print("Number of contributors:", repo.get_contributors().totalCount)
    print("-"*50)
    # # repository content (files & directories)
    # print("Contents:")
    # for content in repo.get_contents(""):
    #     print(content)
    


user = 'kaggle'

repos = getPublicRepositories(user)
# print_repo(repos[1])
for rep in repos:
    print_repo(rep)