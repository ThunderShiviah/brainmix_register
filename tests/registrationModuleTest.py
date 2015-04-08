#!/usr/bin/env python
'''
moduleTest.py
Written by: Kristi Potter
Date: 1/20/15
Purpose: Program to test the registration of lab
images (Modules/module_template.py)
Input: Directory containing jpg images, output directory
Output: Writes registered images to output directory
'''
import sys, os, glob
import numpy as np
sys.path.append("./Modules/")
import module_template as MT
from ITK_AffineRegistration import *
import itk

try:
    import skimage.io
except ImportError:
    sys.exit("please 'pip install scikit-image' to use this script")

# Function to test registration
def registrationModuleTest(inputDir):
    '''
    This function opens all images in a directory,
    converts them to the format for the module,
    passes in the images, and writes the returned
    images to the output directory.
    '''

    #pattern = os.path.join(folder, "*.jpg")
    #average(glob(pattern), os.path.join(folder, "average.jpg"))
    #median(pattern, os.path.join(folder, "median.jpg"))

    # Get all jpg files in directory
    imageFiles = glob.glob(os.path.join(inputDir, '*.jpg'))
    #imageVolume = skimage.io.ImageCollection(imageFiles)
    #print imageVolume
    
    # # Read in the first image and get
    # pic = Image.open(imageFiles[0])
    # imageVolume = np.array(pic.getdata(band=0)).reshape(pic.size[0], pic.size[1], 1)
    # x = pic.size[0]
    # y = pic.size[1]
    # z = len(imageFiles)
    
    # # Read in the rest of the images
    # for i in range(1,z):
    #     pic = Image.open(imageFiles[i])
    #     pix = np.array(pic.getdata(band=0)).reshape(x, y, 1)
    #     imageVolume = np.dstack((imageVolume, pix))

    # Send the image volume to the module, get a volume of images out
    #regImages = MT.moduleTemplate(imageVolume)
    #regImages = ITK_AffineRegistration(imageVolume)
    regImages = ITK_AffineRegistration(imageFiles)
    
    # What to do with output??
    #print regImages

   # pixelType = itk.UC
   # Dimension = 2
   # ImageType = itk.Image[pixelType, Dimension] 
   # ReaderType = itk.ImageFileReader[ImageType] 
    #WriterType = itk.ImageFileWriter[ImageType]
    #CastFilterType = itk.CastImageFilter[ImageType,ImageType]
    #writer = WriterType.New()
    
    #caster = CastFilterType.New()

    
    # for count in range(0, len(regImages)):
    #     # name the output image same as moving image + "aligned" 
    #     writer.SetFileName( "alignedImage%d.jpg" % count) 
    #     #alignedImage = "alignedImage%d.jpg" % count
    #     #count += 1
    #     #print "Outputted: ", alignedImage
    #     print "Size: ", regImages[0].GetLargestPossibleRegion().GetSize()

    #     caster.SetInput( regImages[count-1] )
    #     writer.SetInput( caster.GetOutput() )
    #     writer.Update()
    #     writer.SetSize( regImages[0].GetLargestPossibleRegion().GetSize() )
                
        # adding the aligned image to the list of names of the aligned images
       # self.outputImages.append( alignedImage )
        
    
## -- Wrap main so we can call this via command line -- ##
if __name__ == '__main__':

    p1 = None
    
    if len(sys.argv) != 2:
        print "usage: registrationModuleTest inputDirectory"
        sys.exit()
    else:
        p1 = sys.argv[1]
   
    registrationModuleTest(p1)

