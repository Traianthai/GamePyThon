import imp
import cv2
img = cv2.imread('GamePyThon/dog/enemies/boom/boom.png',10)
print(img.shape) 

# for i in range(0,5):
#     cv2.imwrite(f'boom{i}.png',img[0:179,200*i:200*(i+1)])

# cv2.waitKey(0)