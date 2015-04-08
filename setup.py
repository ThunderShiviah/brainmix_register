
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
	'description': 'A python wrapper for the Allan Brain Institute Mouse Brain Atlas.',
	'author': 'Thunder Shiviah',
	'url': 'https://github.com/ThunderShiviah/AllenBrainAtlasAPI/',
	'download_url': 'git@github.com:ThunderShiviah/AllenBrainAtlasAPI.git',
	'author_email': 'thunder.shiviah@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['allen_api_wrapper'],
	'scripts': [],
	'name': 'allen_api_wrapper'
}

setup(**config)
