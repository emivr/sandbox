import Queue
import threading
import time
import os
import cv2
exitFlag = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      time_before = time.time()
      print "Starting " + self.name
      process_data(self.name, self.q)
      print "Exiting " + self.name
      time_after = time.time()
      print("elapsed time: {}".format((time_after-time_before)))
def process_data(threadName, q):
   time_before = time.time()
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
        data = q.get()
        img = cv2.imread(data,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x,y,w,h) in faces:
            print("face detected in {}".format(data))
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        print("Thread:{}  Processing: {}".format(threadName, data))
        queueLock.release()
      else:
        queueLock.release()
        time.sleep(1)

nameList = []
for x in os.listdir('.'):
    if '.png' in x:
        nameList.append(x)



threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", "Thread-6", "Thread-7","Thread-8"]
queueLock = threading.Lock()
workQueue = Queue.Queue(0)
threads = []
threadID = 7

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print "Exiting Main Thread"
