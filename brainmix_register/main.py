from register_methods import * #I need to change this so I'm not wildcard importin
from pipeline import pipeline
import numpy as np
### For Testing ###
from skimage import io
from skimage.color import rgb2gray

from matplotlib import pyplot as plt


"""The transform pipeline outputs a transform"""
register_pipeline  = pipeline(
        downsample_image,
        #subtract_background,
        #create_binary,
        orb_extractor,
        estimate_transform
        ) 


def registration(stack):
    # TODO: put in a good docstring. I need to figure out what the input type on stack is.
    assert isinstance(stack, list) == True, "stack is not a list: %r" % stack

    transform = register_pipeline(stack)
    show_images(apply_transform(stack, transform)) 
    return transform

if __name__ == "__main__":

    file1 = '../data/p1-D1-01b.jpg'
    file2 = '../data/p1-F4-01b.jpg'

    ''' Read files and convert to grey'''
    img1 = io.imread(file1 ,as_grey=True) # query image
    img2 = io.imread(file2 ,as_grey=True) #training image

    '''convert images to list stack'''
    try:
        stack = [img1, img2]
        assert stack[0].shape == stack[1].shape
        registration(stack)
    except:
       print("registration on {stack_type} failed").format(stack_type=type(stack)) 
