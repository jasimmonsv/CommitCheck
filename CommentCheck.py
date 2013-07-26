'''
Created on Jul 2, 2013

@author: J.A. Simmons V
Program will crawl through a given file directory and look for git comment strings and flag them.
'''

import os, shutil, re, datetime, time
versionNum = 1
startPath = os.getcwd()
crawlPath = 'C:\Program Files\Loansoft'
totalFiles = 0

startTime = datetime.datetime.now()
pattern = re.compile(r"<<<<")
print "Scanning..."
with open('./commentLog.txt', 'a') as commentLog:
	for root, dirs, files in os.walk(crawlPath):
		for e in files:
			totalFiles = totalFiles+1
			with open(os.path.join(root,e),'r') as f:
				rData = f.read()
			f.close()
			target = pattern.search(rData)
			if target: commentLog.write(os.path.join(root,e)+'\n')
	commentLog.close()

endTime = datetime.datetime.now()
with open('./commentLog.txt', 'a') as commentLog:
    commentLog.write('Duration: '+str(endTime-startTime)+'\n')
    commentLog.write('Files scanned: '+str(totalFiles)+'\n')
    commentLog.close()
print "Done!"
