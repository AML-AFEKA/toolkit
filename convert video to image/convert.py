import cv2
import glob
import uuid
import os

for diractory in glob.glob("*"):
    diractory = f'{diractory}\Images'

    for file_path in glob.glob(f'{diractory}\*.wmv'):
        video_object = cv2.VideoCapture(file_path)

        success = True
        i = 0
        while success:
            success,frame = video_object.read()
            if success:
                height, width, _ = frame.shape
                cv2.imwrite(diractory + '\\' + str(uuid.uuid4())[:8] + ".jpg" , frame[100:height, 0: width])
                i += 1

        video_object.release()

        os.remove(file_path)
        print("Done!")
