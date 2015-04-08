# -*- coding: utf-8 -*-
from itertools import islice

import numpy as np

from skimage import io
from skimage.color import rgb2gray
from skimage.transform import pyramid_gaussian
from skimage.filters import threshold_otsu, threshold_adaptive
from skimage import measure
from skimage import img_as_float
from scipy.ndimage import gaussian_filter
from skimage.morphology import reconstruction
from skimage.feature import daisy
from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_harris,
                             corner_peaks, ORB, plot_matches)

from matplotlib import pyplot as plt

"""This module provides a list of functions to aid in registration. 
The design philosophy of each function is to create a 'single input single output' method that will allow for UNIX style piping.

Input to the input layer should be of the form [src, dst] where both src and dst
are numpy arrays of the same size. 

Output of the final 'Apply transform' layer will be of the form [warped_src, dst] where
both src and dst are numpy arrays of the same size as [src, dst].

"""
############# Input layer ##########################

def show_images(stack):
    '''look at the loaded files'''
    f, (ax0, ax1) = plt.subplots(1, 2)
    ax0.imshow(stack[0])
    ax1.imshow(stack[1])
    plt.show()

############# Image pre-processing layer ##########################
def downsample_image(stack):
    """ Returns a stack with each image downsampled.
    
    I use pyramid_gaussian to downsample the images.
    pyramid_gaussian outputs a generator yielding pyramid layers as float images.
    """
    
    """Set parameters"""
    layer = 2
    downscale = 2
    
    """Get downsampled stack"""
    downsampled = [next(islice(pyramid_gaussian(img, downscale=downscale), layer, layer + 1)) for img in stack] #islice gets a single layer from the pyramid.

    
    return downsampled

def subtract_background_generator(stack):
    """ Subtract background"""
    for img in stack:
        # Convert to float: Important for subtraction later which won't work with uint8
        """ image 1 """
        image = gaussian_filter(img, 1)

        seed = np.copy(img)
        seed[1:-1, 1:-1] = img.min()
        mask = img

        dilated = reconstruction(seed, mask, method='dilation')

        img_background_subtracted = img - dilated

        yield(img_background_subtracted)
        
def subtract_background(stack):
    """ Subtract background"""
    subtracted = list(subtract_background_generator(stack))
    return subtracted

def create_binary_generator(stack):
    """ Create global binary """
    for img in stack:
        global_thresh = threshold_otsu(img)
        binary_global = img > global_thresh

        yield(binary_global)
    
def create_binary(stack):
    binary = list(create_binary_generator(stack))
    return binary

################ Feature extraction layer ##############################

def daisy_extractor_generator(stack):
    """ Use daisy binary descriptor to extract features"""
    for img in stack:
        descs, descs_img = daisy(img, step=180, radius=58, rings=2, histograms=6,
                                 orientations=8, visualize=True)
        
        yield(descs) #Currently not yielding the descs_imgs. Do we want those?

def daisy_extractor(stack):
    descriptors = list(daisy_extractor_generator(stack))
    
    """Uncomment this to get descriptor images"""
    #descriptor_imgs = list(daisy_extractor_generator(stack)[1])
    
    return descriptors

def orb_extractor_generator(stack):
    """Orb binary descriptor generator
    
    This returns a descriptor object. The descriptor object encodes both keypoints and descriptors.
    """
    
    """Set parameters"""
    number_of_keypoints=10
    
    """Get descriptor_extractor object"""
    for img in stack:
        descriptor_extractor = ORB(n_keypoints=number_of_keypoints)
        descriptor_extractor.detect_and_extract(img)
        
        yield descriptor_extractor

def orb_keypoints_extractor(stack):
   
    keypoints = list(descriptor_extractor.keypoints for descriptor_extractor in orb_extractor_generator(stack))
    
    return keypoints

def orb_descriptor_extractor(stack):
   
    descriptors = list(descriptor_extractor.descriptors for descriptor_extractor in orb_extractor_generator(stack))
    
    return descriptors 

def match_descriptors_generator(descriptors):
    matches = match_descriptors(descriptors[0], descriptors[1], cross_check=True)
    return(matches)

def get_matching_keypoints(keypoints, descriptors):
    
    matches = match_descriptors_generator(descriptors)
    
    """matches is a nx2 array where the first row refers to the source keypoints and the second row refers to the destination
    coordinates (which are both pairs of xy coordinates). Thus a row in matches of the form
    [i,j]
    means that the ith set of keypoints in the source picture corresponds to the jth set of keypoints in the destination.

    To extract the matching keypoints, I'm using numpy's ndenumerate which is the array version of python's enumerate. The 
    if condition chooses either the source or the destination. I chose to go with an if condition instead of combining the two
    list comprehensions because I thought it enhanced readability. 
    """

    src_match_keypoints = [keypoints[j][value] for (i,j), value in np.ndenumerate(np.array(matches)) if j == 0]

    dst_match_keypoints = [keypoints[j][value] for (i,j), value in np.ndenumerate(np.array(matches)) if j == 1]

    return src_match_keypoints, dst_match_keypoints

def orb_extractor(stack):
    keypoints = orb_keypoints_extractor(stack)
    descriptors = orb_descriptor_extractor(stack)
    src_match_keypoints, dst_match_keypoints = get_matching_keypoints(keypoints, descriptors)
    match_keypoints = [src_match_keypoints, dst_match_keypoints]

    return np.array(match_keypoints)


def show_matches(stack, keypoints, matches):
    
    src = stack[0]
    dst = stack[1]
    
    src_keypoints = keypoints[0]
    dst_keypoints = keypoints[1]
    
    fig, ax = plt.subplots()

    plt.gray()

    plot_matches(ax, src, dst, src_keypoints, dst_keypoints, matches)

    ax.axis('off')

    plt.show()

################### Estimate Transform #######################

def estimate_transform(match_keypoints):

    """ Estimate transform
    Available transformations:
    (‘similarity’, ‘affine’, ‘piecewise-affine’, ‘projective’, ‘polynomial’)
    """
    src_match_keypoints = match_keypoints[0]
    dst_match_keypoints = match_keypoints[1]

    tform = tf.estimate_transform('similarity', src_match_keypoints, dst_match_keypoints)

    """ Error check transform (should return True)"""
    assert  np.allclose(tform.inverse(tform(src_match_keypoints)), src_match_keypoints) == True

    return(tform)

################### Apply Transform ########################

def apply_transform(stack, tform):
    """ Warp image """

    warped = tf.warp(stack[1], inverse_map=tform.inverse) ### Since I'm using the inverse transform, should I apply this to dst?
    warped_stack = [stack[0],warped] 
    return(warped_stack)
