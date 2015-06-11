############# Input layer ##########################
""" Read files and convert to grey"""
as_grey=True

############# Image pre-processing layer ##########################

downscale_dim=2
pyramid_layer=3



#contours = measure.find_contours(contour_in, 0.8, fully_connected='high')

interpolation='nearest', cmap=plt.cm.gray)

################ Feature extraction layer ##############################

""" Use daisy binary descriptor to extract features"""
step=180, radius=58, rings=2, histograms=6,
                         orientations=8, visualize=True)

"""Try orb binary descriptor using binaries created by Otsu's method."""

n_keypoints=100

""" Extract descriptors for the original images """


cross_check=True



################### Estimate Transform #######################

""" Estimate transform
Available transformations:
{‘similarity’, ‘affine’, ‘piecewise-affine’, ‘projective’, ‘polynomial’}
"""

#tform = tf.estimate_transform('similarity', src, dst)

################### Apply Transform ########################

