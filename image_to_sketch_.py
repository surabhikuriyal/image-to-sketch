import imageio

#LOAD IMAGE
img="imagepath"
start_img = imageio.imread(img)

start_img.shape
(196, 160, 30)

# GRAYSCALE
# black and white image: Y= 0.299 R + 0.587 G + 0.114 B
import numpy as np
def grayscale(rgb):
 return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray_img = grayscale(start_img)

# INVERT THE IMAGE
inverted_img = 255-gray_img

# BLUR IMAGE
import scipy.ndimage
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=5)

# DODGE THE IMAGE AND MERGE
def dodge(front,back):
 result=front*255/(255-back) 
 result[result>255]=255
 result[back==255]=255
 return result.astype('uint8')
final_img= dodge(blur_img,gray_img)

# PLOTTING OF IMAGE
import matplotlib.pyplot as plt
plt.imshow(final_img, cmap="gray")

plt.imsave('sketch_img.png', final_img, cmap='gray', vmin=0, vmax=255)
