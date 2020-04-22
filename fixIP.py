hostsFile = '/etc/hosts'
configFile = 'config.production.json'
ipFile = 'jailIP.md'
localIP = '127.0.0.1'

with open(ipFile, 'r') as file :
    jailIP = file.read().strip()

def replaceString(targetFile, searchStr, replaceStr):
    
    with open(targetFile, 'r') as file :
        fileData = file.read()

    fileData = fileData.replace(searchStr, replaceStr)

    with open(targetFile, 'w') as file:
        file.write(fileData)

replaceString(hostsFile, localIP, jailIP)
replaceString(configFile, localIP, jailIP)
replaceString(configFile, 'localhost', jailIP)
