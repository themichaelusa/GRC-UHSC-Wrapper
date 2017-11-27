
def printBlurb(passType, passwords):
	print("Here are", len(passwords), passType, "Ultra-High Security Passwords:")
	for password in passwords:
		print(password)

def getAll(numPass):
	import time
	import requests
	from bs4 import BeautifulSoup

	masterPassList = []
	for i in range(numPass):
		url = 'https://www.grc.com/passwords.htm'
		data = requests.get(url).text
		htm = BeautifulSoup(data, 'lxml')

		allPasswords = []
		allTables = htm.find_all('table', bgcolor='white')
		for table in allTables:
			allPasswords.append(table.find('font').text)
		allPasswords = tuple(allPasswords[:3])
		masterPassList.append(allPasswords)
		time.sleep(.1)

	zippedLists = list(zip(*masterPassList))
	return {
	'HEX': zippedLists[0],
	'ASCII': zippedLists[1],
	'ANUM': zippedLists[2]
	}

def getPass(passType, numPass):
	passTypes = ['HEX', 'ASCII', 'ANUM']
	if (passType in passTypes):
		masterPassList = getAll(numPass)
		passwords = masterPassList[passType]
		printBlurb(passType, passwords)
	else: 
		print("Please Enter A Valid Password Type Like:", passTypes)
