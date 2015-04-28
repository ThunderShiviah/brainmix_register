import skimage as sk
import sys, os, glob


def register(dir):
    pass

if __name__ == "__main__":

    inputDir = '../data'
    # Get all jpg files in directory
    imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    data = sk.io.ImageCollection(imageFiles, as_grey=True).concatenate()


    registered_data = register(data)
    assert registered_data.size == data.size
    
