# Brainmix_register: A registration method built using scikit-image for the University of Oregon brainmix project. 

brainmix_register is a python image registration library built on [scikit-image](http://scikit-image.org/) (see [this page](http://nbviewer.ipython.org/github/ThunderShiviah/brainmix_register/blob/master/docs/registration_demo.ipynb) for a demo using ipython notebook).

# Installation
Currently, brainmix_register is being developed using python 2.7. The recommended way to install is by downloading the repository via github:

```
git clone git@github.com:ThunderShiviah/brainmix_register.git 
```

Then navigate to the top directory  (the directory containing setup.py) and run the following command:

```
python setup.py install
```

To uninstall use pip:
```
pip uninstall brainmix_register
```

To run tests, navigate to the directory above tests and run the following command:
```
nosetests
```
# License
The MIT License (MIT)

Copyright (c) [2015] [Thunder Shiviah]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
