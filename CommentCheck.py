'''
Created on Jul 2, 2013

@author: J.A. Simmons V
Program will crawl through a given file directory and look for git comment strings and flag them.
'''

import os
import shutil
import re
versionNum = 1
startPath = os.getcwd()
changeFiles = 0
totalFiles = 0
print "Scanning..."
pattern = re.compile(r"<<<<")

with open('./commentLog.txt', 'w') as commentLog:
	for root, dirs, files in os.walk('C:\Program Files\Loansoft'):
		for e in files:
			totalFiles = totalFiles+1
			with open(os.path.join(root,e),'r') as f:
				rData = f.read()
			f.close()
			target = pattern.search(rData)
			if target: commentLog.write(os.path.join(root,e)+'\n')
	commentLog.close()
            
print totalFiles
print "Done!"
