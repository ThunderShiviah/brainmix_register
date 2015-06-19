#!/usr/bin/env python
from matplotlib import pyplot as plt
from brainmix_register import data
from brainmix_register.registration.registration import main as register
from brainmix_register.registration.registration import overlay_pics
from skimage import io

def demo():
    """Loads an example image stack from data.test_stack() and registers the
    stack using the main register function in sub-package registration. 
    Returns data about stack type, stack dimensions. Displays the pre and 
    post registered stack.
    
    Takes no arguments."""

    stack = data.test_stack()
    reg_stack = register(stack)

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

if __name__ == "__main__":
    demo()

