import multiprocessing
import time
import os
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

data = []
for f in os.listdir('.'):
    if '.png' in f:
        data.append(f)
print(len(data))

def mp_worker(inputs):
    img = cv2.imread(inputs,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        print("face detected: {}".format(inputs))
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
def mp_handler():
    p = multiprocessing.Pool(8)
    p.map(mp_worker, data)

if __name__ == '__main__':
    time_before = time.time()
    mp_handler()
    finaltime = (time.time()-time_before)
    print(finaltime)
