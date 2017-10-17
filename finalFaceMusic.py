import cv2
import pygame
import time
import threading
#Initialise pygame and the mixercd ~/opencv


def sound():
    pygame.init()
    pygame.mixer.init()
    mysound = pygame.mixer.Sound("/home/aksh/Downloads/ambulancehorn2.wav")
    mysound.play()
    time.sleep(5)
    mysound.stop()



def cascade():
    faceCascade = cv2.CascadeClassifier('/home/aksh/Downloads/haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)


    return video_capture,faceCascade

def loop():

    video_capture,faceCascade = cascade()

    while True:

        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE

        )

        f = len(faces)
        # print  f
        # time.sleep(8)
        if f == 0:
            print ('Not Detected')

        else:
            print(f)
            video_capture.release()
            threads = []
            t = threading.Thread(target=sound())
            threads.append(t)
            t.start()
            loopind()

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        #cv2.imshow('Video', frame)
        # mysound.stop()


        # raw_input("enter")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

            # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()



def loopind():

    while True:
        t = threading.Thread(target=loop())
        t.start()
        # a = threading.Thread(target=loop())
        # t.start()



loopind()

