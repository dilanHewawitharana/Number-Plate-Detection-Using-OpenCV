import cv2

######################################
numberPlateCascade = cv2.CascadeClassifier('Resources/haarcascade_russian_plate_number.xml')

imageWidth = 640
imageHeight = 480
minArea = 500
color = (0, 0, 255)
count = 0

#####################################

# Camera read
cap = cv2.VideoCapture('Resources/video.avi')
cap.set(3, imageWidth)
cap.set(4, imageHeight)
cap.set(10, 100)  # Set Brightness

while True:
    success, img = cap.read()
    img = cv2.resize(img, (imageWidth, imageHeight))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlate = numberPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            # cv2.putText(img, 'Number Plate detected', (x, y-5),
            #             cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('ROI', imgRoi)

    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Resources/Scanned/NoPlate_'+str(count)+'.jpg', imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, 'Scanned and Saved', (150, 265), cv2.FONT_HERSHEY_TRIPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow('Video', img)
        cv2.waitKey(500)
        count += 1
