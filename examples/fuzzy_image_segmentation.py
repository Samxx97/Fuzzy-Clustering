

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import img_as_float
from fuzzy_clustering.core.fuzzy import FCM
from fuzzy_clustering.utils.utils import segment_image


def sample_fcm_image():
    
    _, axis = plt.subplots(1,2, figsize= (8,6))
    axis = axis.flatten()
    
    
    #Loading image
    img = cv2.imread('..//res//oarsman.jpeg')
    img = img_as_float(img)
    x = np.reshape(img,(img.shape[0]*img.shape[1],3),order='F')
    
    verbose =0
    m,c = FCM(x,c=10)
    labels = m.argmax(axis=1)
    
    m = np.reshape(labels,(img.shape[0],img.shape[1]),order='F').astype('int64')
    
    #Replace pixel intensity with centers found by FCM or replace pixel intensity with median for each cluster
    sigm_img = segment_image(img,m,c,verbose)
    
    
    imgs = [img, sigm_img]
    for image,ax in zip(imgs,axis):
        ax.imshow(image[:,:,::-1])
    
    #Preview output image
    plt.show()
    

if __name__ == "__main__":
    sample_fcm_image()