import os as _os

from skimage.io import imread, use_plugin

__all__ = ['load',
        'all',
        'test']

def load(f):
    """Load an image file located in the data directory.
    
    Parameters
    ----------
    f : string
        File name.

    Returns
    -------
    img : ndarray
        Image loaded from skimage.data_dir.
    """
    use_plugin('pil')
    return imread(_os.path.join(data_dir, f))

def test():
    inputDir = '/test/'
    imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    imageVolume = io.ImageCollection(imageFiles, as_grey=True).concatenate()
    return imageVolume

