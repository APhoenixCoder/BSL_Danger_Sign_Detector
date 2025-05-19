import numpy as np
import cv2

#import tensorflow as tf

#model=tf.keras.models.load_model('keras_model.h5')
#print(model)



# Open the default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Read frame-by-frame
    ret, frame = cap.read()

    # If frame not read correctly
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Show the frame in a window
    cv2.imshow('Webcam Feed', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
