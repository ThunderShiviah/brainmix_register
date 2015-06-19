from brainmix_register import data

def import_test():
    try:
        from brainmix_register import data
    except:
        assert False

def load_image_test():
    
    data.image()

def check_image_shape_length_test():

    test =  data.image()
    assert len(test.shape) == 2  # Shape should be 2 because img is gray. 

def check_image_shape_test():
    test = data.image()
    assert test.shape == (1040, 1388)
def load_test_stack_test():
    data.test_stack()

def check_test_stack_shape_length_test():

    stack = data.test_stack()
    assert len(stack.shape) == 3
    
def check_test_stack_shape_test():
    stack = data.test_stack()
    assert stack.shape == (3, 1040, 1388)
def load_large_stack_test():

    data.all_stack()

def check_large_stack_shape_length_test():

    test = data.all_stack()
    assert len(test.shape) == 3 

def check_large_stack_shape_test():

    test = data.all_stack()
    assert test.shape == (18, 1040, 1388) 



    
