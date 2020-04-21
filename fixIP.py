targetFile = 'config.production.json'
searchStr = '127.0.0.1'
jailIP = 'jailIP.md'

with open(jailIP, 'r') as file :
    replaceStr = file.read()

# Read in the file
with open(targetFile, 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace(searchStr, replaceStr.strip())

# Write the file out again
with open(targetFile, 'w') as file:
    file.write(filedata)
