import sys, os, glob
from skimage import io
from skimage import viewer
import registration as reg
from skimage import data

def display():
    pass


if __name__ == "__main__":
    # ------------------Create input ndarray------------------------
    inputDir = '../data/test/'
    imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    imageVolume = io.ImageCollection(imageFiles, as_grey=True).concatenate()
    stack = imageVolume

    # ------------------Check that single image registration works----

    src = stack[0]
    dst = stack[1]

    reg_dst = reg.reg(src, dst)

    # ------------- Check that stack registration works -----------
    
    reg_stack = reg.registration(stack)

    merged = [reg.overlay_pics(stack[0], img) for img in stack]
    merged_reg = [reg.overlay_pics(reg_stack[0], img) for img in reg_stack]
    image = data.coins()

    viewer = viewer.CollectionViewer(merged_reg)
    viewer.show()

