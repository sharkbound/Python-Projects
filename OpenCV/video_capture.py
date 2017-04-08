import cv2
import numpy as np
from datetime import datetime


def entry():
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('../../video.avi', codec, 20.0, (width, height))

    previous_frame = None
    previous_frame_update_delay_seconds = 15
    previous_frame_last_update = datetime.now()

    loop = 0

    while True:
        feed_valid, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if feed_valid:
            cv2.imshow('FRAME', frame)
            # cv2.imshow('GRAY', gray)

            if previous_frame is not None:
                cv2.imshow("PREVIOUS", previous_frame)

            try:
                out.write(frame)
            except:
                print('error writing frame, skipping...')

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        if (datetime.now() - previous_frame_last_update).seconds >= previous_frame_update_delay_seconds:
            previous_frame = frame
            previous_frame_last_update = datetime.now()

        loop += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    entry()
