import cv2
import os

image = cv2.imread("C:/Users/Gido/Documents/workspace/development/workshop_aaec_revamp/src/workshop_aaec_revamp/rgb_qrdepth_Color.png")

qrCodeDetector = cv2.QRCodeDetector()

decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
print(points)
if points is not None:
 
    nrOfPoints = len(points[0])
 
    for i in range(nrOfPoints):
        nextPointIndex = (i+1) % nrOfPoints
        cv2.line(image, (int(points[0][i][0]), int(points[0][i][1])) , (int(points[0][nextPointIndex][0]), int(points[0][nextPointIndex][1])), (255,0,0), 5)
 
    print(decodedText)    
 
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
 
else:
    print("QR code not detected")


# Todo match the pixels to the pointcloud.