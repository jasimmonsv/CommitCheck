'''
Created on Jul 2, 2013

@author: J.A. Simmons V
Program will crawl through a given file directory and look for git comment strings and flag them.
'''

import os, shutil, re, datetime, time, threading, Queue
versionNum = 1
startPath = os.getcwd()
crawlPath = 'C:\Program Files\Loansoft'
totalFiles = 0
threadCount = 5
dirtyFiles = []
queueFiles=[]
pattern = re.compile(r"<<<<")
queue = Queue.Queue()

class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue=queue

    def run(self):
        while True:
            file=self.queue.get()
            with open(file,'r') as f:
                rData = f.read()
            f.close()
            target = pattern.search(rData)
            if target: dirtyFiles.append(file)
            self.queue.task_done()
	
def main():
	for root, dirs, files in os.walk(crawlPath):
		for e in files:
			if root.find('.git') == -1: queue.put(os.path.join(root,e))
	print 'Total files: '+str(queue.qsize())
	
	for i in range(threadCount):
		t=ThreadClass(queue)
		t.setDaemon(True)
		t.start()
	
	queue.join()
	
print "Scanning..."
startTime = datetime.datetime.now()
main()
endTime = datetime.datetime.now()
print "Writing log...\n"
with open('./commentLog.txt', 'a') as commentLog:
    for i in range(len(dirtyFiles)):
	    commentLog.write(dirtyFiles[i]+'\n')
    commentLog.write('Duration: '+str(endTime-startTime)+'\n')
    commentLog.close()
print "Elapsed Time: %s" % (endTime-startTime)
print "Done!"
