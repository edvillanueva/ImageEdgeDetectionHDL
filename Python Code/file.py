import cv2
import numpy
img = cv2.imread('minirod.jpg')
ret,gray = cv2.threshold(img,127,256,cv2.THRESH_BINARY)
cv2.imshow('Original Image',img)
cv2.imshow('Binary Image',gray)

with open('binaryfile.csv','w') as f:
    for row in gray:
        TMP = ''
        for col in row:
            TMP += '{0}, '.format(col[0])
        TMP.rstrip(', ')
        f.write(TMP+'\n')
f.close()

cv2.waitKey(0)

