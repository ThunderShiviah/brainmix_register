import os, glob
from nose.tools import *
import brainmix_register.registration as reg
import skimage
from skimage import io

# ------------------Create input ndarray------------------------
# TODO: Convert this into a set-up decorator.
def setup():
    inputDir = '../data/test/'
    imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    #imageVolume = io.ImageCollection(imageFiles, as_grey=True).concatenate()
    #stack = imageVolume
    return imageFiles




def teardown():
    print("TEAR DOWN!")

def test_basic():
    imageFiles = setup()
    print("I RAN!")
    print(imageFiles)


