#!/usr/bin/python
import cv2
import threading
import time
import sys
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
class myThread (threading.Thread):
   def __init__(self, threadID, name,processpicture):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.processpicture = processpicture
   def run(self):
      print "Starting " + self.name
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.processpicture)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName,processpicture):
    print("threadname: {} picture for processing {}".format(threadName, processpicture))
    img = cv2.imread(processpicture,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        print("face in {}".format(processpicture))
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

threadLock = threading.Lock()
threads = []

# Create new threads
i=0
time_before = time.time()
for img in os.listdir(sys.argv[1]):
    if '.png' in img:
        name = 'Thread'+str(i)
        workerbee = myThread(1, name, img)
        i=i+1
# Start new Threads
        workerbee.start()
# Add threads to thread list
        threads.append(workerbee)
        print(len(threads))
    # Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"

time_after = time.time()

print("total time elapsed: {}".format((time_after-time_before)/60))
