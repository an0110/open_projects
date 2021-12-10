# import cv2
#
# originalImage = cv2.imread(r"D:\work\20160402_125316.jpg")
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
#
# testingImage = cv2.cvtColor(originalImage, cv2.CALIB_CB_NORMALIZE_IMAGE)
#
#
# (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
#
# # cv2.imshow('Black white image', blackAndWhiteImage)
# # cv2.imshow('Original image', originalImage)
# # cv2.imshow('Gray image', grayImage)
# #
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # cv2.imw
# # cv2.imwrite(r"D:\work\20160402_125316_c.jpg", grayImage)
# cv2.imwrite(r"D:\work\20160402_125316_c.jpg", testingImage)



from PIL import Image

originalImage = Image.open(r"D:\work\20160402_125316.jpg")
print (originalImage.mode)
cy = originalImage.convert('UCR')
print (cy)
originalImage.save (r"D:\work\20160402_125316_d.jpg")





