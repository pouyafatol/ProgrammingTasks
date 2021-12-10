import os
import re
import requests

def getFilesPath(sourceDirPath):
    filesPath = []
    for root, dirs, files in os.walk(sourceDirPath):
        for name in files:
            filesPath.append(os.path.join(root, name))
    return filesPath

def findLinks(filesPathList):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    links = []   
    for fp in filesPathList:
        with open(fp,'rb') as file:
            for line in file.readlines():
                urls = re.findall(regex, line.decode('utf-8')) 
                _ = [links.append(x[0]) for x in urls]
    return links

def checkStatusCodeAndReport(links):
    success,redirection,clientError,serverError,invalidLinkes = [],[],[],[],[]

    for link in links:
        try:
            response = requests.get(link)
            status = response.status_code
            if 200 <= status <= 299:
                success.append(link)

            elif 300 <= status <= 399:
                redirection.append(link)

            elif 400 <= status <= 499:
                clientError.append(link)

            elif 500 <= status <= 599:
                serverError.append(link)

        except:
            invalidLinkes.append(link)

    noOfTotalLinks = len(links)
    noOfInvalidLinks = len(invalidLinkes)
    validity = (noOfTotalLinks-noOfInvalidLinks)/noOfTotalLinks * 100

    print(f'{len(success)} Success links')
    print(f'{len(redirection)} Redirection links')
    print(f'{len(clientError)} Client error links')
    print(f'{len(serverError)} Server error links')
    print(f'Total link’s validity: {validity}%')

def main():
    dirName = 'test'
    sourceDirPath = os.path.join(os.getcwd(),dirName)

    filesPath = getFilesPath(sourceDirPath)
    links = findLinks(filesPath)
    checkStatusCodeAndReport(links)

if __name__ == '__main__':
    main()