from brainmix_register import data

def import_test():
    try:
        from brainmix_register import data
    except:
        assert False

def load_file_test():
    
    data.image()

def check_file_shape_test():

    test =  data.image()
    assert len(test.shape) == 3  # Should this be a separate test?  

def load_stack_test():
    data.test_stack()

def check_stack_shape_test():

    stack = data.test_stack()
    assert len(stack.shape) == 3
    
def load_large_stack_test():

    data.all_stack()

def check_large_stack_test():

    test = data.all_stack()
    assert len(test.shape) == 3 
    
