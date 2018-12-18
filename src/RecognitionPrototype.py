# Necessary libraries
import cv2
import datetime
import time
import face_recognition
import os
import numpy

# Initialize video capture on default device (webcam)
camera = cv2.VideoCapture(0)

# Timer before the capture is created
print('Please look directly at the camera. Photo will be taken in 5 seconds.')
timer = 5
while timer > 0:
    print(timer)
    time.sleep(1)
    timer -= 1

# Prepare name of the image
temporaryImage = datetime.datetime.today().strftime('%Y-%m-%d %H:%M.jpg')

while True:
    # Read camera capture and write to file
    ret, frame = camera.read()
    cv2.imwrite(temporaryImage, frame)

    print('Photo was taken.')
    break

# Release the camera capture and destroy all windows
camera.release()
cv2.destroyAllWindows()

# Load the image you've just acquired and encode it into a feature vector
imageForMatch = face_recognition.load_image_file(temporaryImage)
imageForMatchEncoded = face_recognition.face_encodings(imageForMatch)[0]

# Dataset
dataset = os.listdir(os.getcwd() + '/faceData')

# Loop through all images
for image in dataset:
    # Extract the name out of the image file
    name = str(image)[:-7]

    #Use the first image in the dataset
    if image.startswith(name) and image.endswith('001.jpg'):

        #Load this image, encode into a feature vector and make a comparison with the taken image
        datasetImage = face_recognition.load_image_file(os.getcwd() + '/faceData/' + image)
        datasetImageEncoded = face_recognition.face_encodings(datasetImage)[0]
        result = face_recognition.compare_faces([imageForMatchEncoded], datasetImageEncoded)

        # Compare results
        if result[0] == True:
            print('Match: %s' % name)
        else:
            print('No match. Access denied. This incident will be reported.')
