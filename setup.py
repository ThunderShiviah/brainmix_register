
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
	'description': 'A python image registration module using scikit image.',
	'author': 'Thunder Shiviah',
	'url': 'https://github.com/ThunderShiviah/brainmix_register/',
	'download_url': 'git@github.com:ThunderShiviah/brainmix_register.git',
	'author_email': 'thunder.shiviah@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['brainmix_register'],
	'scripts': [],
	'name': 'brainmix_register'
}

setup(**config)
