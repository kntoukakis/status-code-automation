#!/usr/local/bin/python
import urllib
from status_codes import check_status

readFile=open('websites.txt','r')
websites=readFile.read().split('\n')
readFile.close()

#print (websites)

file = open("results.txt", "w")

for website in websites:
	
	try:
		a = urllib.urlopen(website)
		status = a.getcode()

		result = check_status(status)
		message = " %s %s" %(website,result)
		print (message)
		file.write(("%s\n" % message))

	except:
		exception = " %s doesn't exist" % (website)
		print (exception)
		file.write(("%s\n" % exception))

file.close()