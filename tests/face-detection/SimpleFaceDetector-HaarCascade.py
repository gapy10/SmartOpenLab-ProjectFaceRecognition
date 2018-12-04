# Necessary libraries
import cv2

# Load XML classifiers (Haar cascade)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Capture video from built-in web camera
capture = cv2.VideoCapture(0)

while True:
    # Grab, decode and return video frame
    ret, image = capture.read()

    # Applies an adaptive threshold to an array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect objects (faces), return list of rectangles
    faces = faceCascade.detectMultiScale(gray, 1.3, 3)

    for (x, y, w, h) in faces:
        # Draw a rectangle around detected face (blue)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roiGray = gray[y:y+h, x:x+w]
        roiColor = image[y:y+h, x:x+w]

        # Draw a rectangle around detected eyes (green)
        eyes = eyeCascade.detectMultiScale(roiGray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColor, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Draw a rectangle around detected smiles or mouths (red)
        smiles = smileCascade.detectMultiScale(roiGray)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roiColor, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    # Display an image in the specified window (window is what camera sees)
    cv2.imshow('image', image)

    # Create trackbar and attach it to the specified window
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

# Close capturing device + "destroy" GUI window
capture.release()
cv2.destroyAllWindows()
