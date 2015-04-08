from register_methods import * #Is this a bad idea? In this case I don't see risk of collision.
from pipeline import pipeline
import numpy as np

"""The transform pipeline outputs a transform"""
register_pipeline  = pipeline(
        downsample_image,
        subtract_background,
        create_binary,
        orb_extractor,
        estimate_transform
        ) 

        
def registration(stack):
    # TODO: put in a good docstring. I need to figure out what the input type on stack is.
    assert isinstance(stack, list) == True, "stack is not a list: %r" % stack

    transform = register_pipeline(stack)
    show_images(apply_transform(stack, transform)) 
    
