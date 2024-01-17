import cv2


img = cv2.imread('assets/image1.jpg',0)

#resize image
# img = cv2.resize(img,(400,400))
# rotate image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('new_image.jpg',img)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
