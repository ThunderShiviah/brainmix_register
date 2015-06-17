import numpy as np

def import_registration_test():
    try:
        from brainmix_register import registration
    except:
        assert False

from brainmix_register.registration import registration
from brainmix_register import data

def reg_function_test():
    stack = data.test_stack()
    src = stack[0]
    dst = stack[1]
    registration.reg(src, dst)
    
def reg_function_same_image_test():
    """Checks that registering an image to itself leaves
    the image unchanged."""
    stack = data.test_stack()
    src = stack[0]
    dst = stack[0]
    reg_dst = registration.reg(src, dst)
    if not np.array_equal(reg_dst, dst):
        assert False
     
def check_that_src_dst_are_not_equal_test():
    stack = data.test_stack()
    src = stack[0]
    dst = stack[1]
    if np.array_equal(src, dst):
        assert False
    
def reg_function_different_image_test():
    """Checks that registering an image to a different image changes
    the image."""
    stack = data.test_stack()
    src = stack[0]
    dst = stack[1]
    reg_dst = registration.reg(src, dst)
    if np.array_equal(reg_dst, dst):
        assert False
 
def reg_iter_function_test():
    stack = data.test_stack()
    reg_stack = registration.reg_iter(stack) 
    
def reg_iter_function_same_src_test():
    """First image in both pre and post registered stack is used as
    the target image so should be unchanged in both cases."""
    stack = data.test_stack()
    reg_stack = registration.reg_iter(stack) 
    if not np.array_equal(stack[0], reg_stack[0]):
        assert False

def reg_iter_function_test():
    stack = data.test_stack()
    reg_stack = registration.reg_iter(stack) 
    if np.array_equal(stack[0], reg_stack[1]):
        assert False

def overlay_pics_test():
    stack = data.test_stack() 
    src = stack[0]
    dst = stack[1]
    registration.overlay_pics(src, dst)

def overlay_same_pics_test():
    """Overlaying a picture with itself should produce the original pic"""
    stack = data.test_stack() 
    src = stack[0]
    dst = stack[0]
    overlayed_img = registration.overlay_pics(src, dst)
    if np.array_equal(src, overlayed_img):
        assert False

def main_test():
    stack = data.test_stack()
    registration.main(stack)

def main_src_test():
    """Check that the target images in pre and post registered
    stack are unchanged"""
    stack = data.test_stack()
    reg_stack = registration.main(stack)
    if not np.array_equal(stack[0], reg_stack[0]):
        assert False

def main_dst_reg_dst_are_different_test():
    """Check that the destination images in pre and post registered
    stack are different"""
    stack = data.test_stack()
    reg_stack = registration.main(stack)
    if np.array_equal(stack[1], reg_stack[1]):
        assert False

def main_size_test():
    stack = data.test_stack()
    reg_stack = registration.main(stack)
    assert stack.shape == reg_stack.shape




