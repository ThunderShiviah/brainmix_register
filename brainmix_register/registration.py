import sys, os, glob
import numpy as np
sys.path.append("../Modules/")
from skimage import io

from skimage import data
from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_harris,
                             corner_peaks, ORB, plot_matches)
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

#-----------------Registration function-------------------------

def reg(src, dst):
    """Takes in a source and destination image and returns a registered source image.
    """
    
    src = orb_reg(src, dst)
    return src

#----------------Stack function --------------------------------

def reg_iter(stack):
    """Takes a stack of images and registers each one using the first image as the destination. 
    output: a registered stack.
    """
    dst = stack[0]
    reg_stack = [reg(src, dst) for src in stack]
    return reg_stack

#---------------main-------------------------------
def main_reg(img_stack):
    """input: ndarray of images
    ouput: ndarray of registered images
    """
    reg_stack = reg_iter(img_stack)
    #assert np.array_equal(img_stack[0], reg_stack[0]) #dst images should be the same 
    if not np.array_equal(img_stack[0], reg_stack[0]):
        print("destination image has been changed in registered stack.")
    assert not np.array_equal(img_stack[0], reg_stack[1]) #src and dst images should be different
    #return type(reg_stack)
    return io.concatenate_images(reg_stack)

def orb_reg(src, dst, viz=False):
    img1 = src
    img2 = dst
    tform = tf.AffineTransform(scale=(1.3, 1.1), rotation=0.5,
                               translation=(0, -200))
    img3 = tf.warp(img1, tform)

    descriptor_extractor = ORB(n_keypoints=200)

    descriptor_extractor.detect_and_extract(img1)
    keypoints1 = descriptor_extractor.keypoints
    descriptors1 = descriptor_extractor.descriptors

    descriptor_extractor.detect_and_extract(img2)
    keypoints2 = descriptor_extractor.keypoints
    descriptors2 = descriptor_extractor.descriptors

    descriptor_extractor.detect_and_extract(img3)
    keypoints3 = descriptor_extractor.keypoints
    descriptors3 = descriptor_extractor.descriptors

    matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)
    matches13 = match_descriptors(descriptors1, descriptors3, cross_check=True)

    if viz == True:
        fig, ax = plt.subplots(nrows=2, ncols=1)

        plt.gray()

        plot_matches(ax[0], img1, img2, keypoints1, keypoints2, matches12)
        ax[0].axis('off')

        plot_matches(ax[1], img1, img3, keypoints1, keypoints3, matches13)
        ax[1].axis('off')

        plt.show()
        
    return img3

if __name__ == "__main__":
    #------------------Create input ndarray------------------------
    inputDir = '../test/'
    imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    imageVolume = io.ImageCollection(imageFiles, as_grey=True).concatenate()
    stack = imageVolume

    reg_arr = main_reg(stack)
    print(type(reg_arr))

