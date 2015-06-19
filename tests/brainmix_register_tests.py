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

def import_data_package_test():
    try:
        from brainmix_register import data
    except:
        assert False

def import_demo_package_test():
    try:
        from brainmix_register import demo
    except:
        assert False, 'Cannot import demo'

def import_display_package_test():
    try:
        from brainmix_register import display
    except:
        assert False, 'Cannot import display'

def import_registration_package_test():
    try:
        from brainmix_register import registration
    except:
        assert False, 'Cannot import registration'

def import_utils_package_test():
    try:
        from brainmix_register import utils
    except:
        assert False, 'Cannot import utils'



