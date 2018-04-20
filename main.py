import numpy as np
from PIL import ImageGrab
import cv2
import time


def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=150, threshold2=150)
    return processed_image

def screen_record():
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox =(125,125,925,725)))
        new_screen = process_image(screen)
        
        print("Loop took {} seconds".format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',new_screen)
        #cv2.imshow('window',cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


screen_record()
