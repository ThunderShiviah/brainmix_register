from nose.tools import *
import brainmix_register
import skimage


def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")

def try_registration(stack):
    try:
        brainmix_register.main(registration)
    except:
        print("Registration on {stack_type failed}").format(stack_type=type(stack))

 
def test_list_of_two_images():
    """ A test to check if the registration function in main can run a list of two ndarray images.

    input: a list of two ndarray images
    """
    file1 = "../data/p1-D1-01b.jpg"
    file2 = "../data/p1-F4-01b.jpg"
    
    """ Read files and convert to grey """
    img1 = skimage.io.imread(file1, as_gray=True) #query image
    img2 = skimage.io.imread(file2, as_gray=True) #training image
    
    stack = [img1, img2]


def check_that_stack_is_same_size(stack):
    """ Checks that every image in the stack has the same dimensions
    input: a stack of images
    """
    for image in stack:
        assert image.shape == stack[0].shape
