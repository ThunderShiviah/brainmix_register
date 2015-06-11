"""Brain test images"""
import glob
import os 
from skimage import io
from . import all, test
from skimage.io import imread, use_plugin

def load_image(file_name, inputDir):
    """Loads an image."""

    use_plugin('pil')
    return imread(os.path.join(inputDir, file_name))

def load_stack(inputDir):

    """Loads .jpg files from a directory and concatenates into an image stack\
     using io.ImageCollection."""

    print(inputDir)
    imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    imageVolume = io.ImageCollection(imageFiles, as_grey=True).concatenate()
    return imageVolume

def image():
    """Load a single image from p1 brain directory.
    output: a single image as a numpy array"""


    inputDir = '{}'.format(all.__path__[0])
    return load_image('p1-D3-01b.jpg',inputDir)

def test_stack():
    """Load a stack from the test directory.
    output: a numpy array of images (gray scale)."""

    inputDir = '{}'.format(test.__path__[0])
    return load_stack(inputDir)
    
def all_stack():
    """Load a stack from the test directory.
    output: a numpy array of images (gray scale)."""

    inputDir = '{}'.format(all.__path__[0])
    return load_stack(inputDir)
 
    


