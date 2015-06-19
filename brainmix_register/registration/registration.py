import sys
import os, glob
import numpy as np
from skimage import feature
from skimage import io
from skimage import transform as tf
import matplotlib.pyplot as plt
from skimage.color import gray2rgb
from brainmix_register import data  # Should this be a relative import?


# -----------------Registration function-------------------------


def reg(src, dst):
    """Takes in a source and destination image and returns a
    registered destination (target) image. Note: This registration method
    is a rigid translation. See scikit-image 
    feature.register_translation for more information

    src: the reference image
    dst: the image to register

    """
    upsample_factor = 100
    shifts, err, phasediff = feature.register_translation(src, dst, \
    upsample_factor)
    tform = tf.AffineTransform(translation=shifts[::-1])
    reg_dst = tf.warp(dst, inverse_map=tform.inverse)

    return reg_dst

# ----------------Stack function --------------------------------


def reg_iter(stack):
    """
    input: a stack of images and registers each one using the first
    image as the source.
    output: a registered stack.
    """
    src = stack[0]
    reg_stack = [reg(src, dst) for dst in stack]
    return reg_stack

# --------------View overlayed result--------------------------


def overlay_pics(src, dst):

    image0_ = src
    image1_ = dst

    def add_alpha(image, background=-1):
        """Add an alpha layer to the image.

        The alpha layer is set to 1 for foreground
        and 0 for background.
        """
        rgb = gray2rgb(image)
        alpha = (image != background)
        return np.dstack((rgb, alpha))

    image0_alpha = add_alpha(image0_)
    image1_alpha = add_alpha(image1_)

    merged = (image0_alpha + image1_alpha)
    alpha = merged[..., 3]

    # The summed alpha layers give us an indication of
    # how many images were combined to make up each
    # pixel.  Divide by the number of images to get
    # an average.
    merged /= np.maximum(alpha, 1)[..., np.newaxis]
    return merged

# ---------------main-------------------------------


def main(img_stack):
    """input: ndarray of images
    ouput: ndarray of registered images
    """

    # assert len(img_stack) == 3  # Check that images are greyscale.
    reg_stack = reg_iter(img_stack)

    if not np.array_equal(img_stack[0], reg_stack[0]):
        assert False, "destination image has been changed in registered stack."
    # src and dst images should be different
    assert not np.array_equal(img_stack[0], reg_stack[1])
    return io.concatenate_images(reg_stack)

if __name__ == "__main__":
    # Check if running with version 2 or 3. If 2, use raw_input().
    # Currently, python 3 causes the script to exit.
    # TODO: if v. 3, then parse commandline arguments with input()
    # else, use raw_input().

    if sys.version_info >= (3,0):
        sys.stdout.write("Sorry, requires Python 2.x, not Python 3.x\n")
        sys.exit(1)
    
    if len(sys.argv) == 2: 
        inputDir = sys.argv[-1] 
        imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
        imageVolume = io.ImageCollection(imageFiles, as_grey=True).concatenate()
        stack = imageVolume

        reg_stack = main(stack)
        i = 0;
        for img in reg_stack:
            io.imsave('reg{}',img).format(i)
            i += 1
        sys.exit(1)


    elif len(sys.argv) > 2: 
        print("Script takes in one or zero arguments.")
        sys.exit(1)

    else: 
        inputDir = '../data/test/'
    
    # ------------------Create input ndarray------------------------
    #imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    #imageVolume = io.ImageCollection(imageFiles, as_grey=True).concatenate()
    #stack = imageVolume

    # reg_stack = main(stack)
    stack = data.test_stack()
    reg_stack = main(stack)

    print('stack is of type', type(stack))
    print('stack dimensions are', stack.shape)
    print('registered stack is of type', type(reg_stack))
    print('registered stack dimensions are', reg_stack.shape)

    merged = [overlay_pics(stack[0], img) for img in stack]
    merged_reg = [overlay_pics(reg_stack[0], img) for img in reg_stack]
    fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(8, 5))

    plt.gray()

    ax[0, 0].imshow(merged[0])
    ax[0, 0].axis('off')
    ax[0, 0].set_title('original 1-1')
    ax[0, 1].imshow(merged[1])
    ax[0, 1].axis('off')
    ax[0, 1].set_title('original 1-2')
    ax[0, 2].imshow(merged[2])
    ax[0, 2].axis('off')
    ax[0, 2].set_title('original 1-3')

    ax[1, 0].imshow(merged_reg[0])
    ax[1, 0].axis('off')
    ax[1, 0].set_title('registered 1-1')
    ax[1, 1].imshow(merged_reg[1])
    ax[1, 1].axis('off')
    ax[1, 1].set_title('registered 1-2')
    ax[1, 2].imshow(merged_reg[2])
    ax[1, 2].axis('off')
    ax[1, 2].set_title('registered 1-3')

    fig.subplots_adjust(wspace=0.02, hspace=0.2,
                        top=0.9, bottom=0.05, left=0, right=1)

    plt.show()
