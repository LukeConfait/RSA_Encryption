try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple RSA encryption implementation',
    'author' : 'Luke Confait',
    'url' : 'URL to get it at',
    'download_url' : 'Where to download it.',
    'author_email' : 'luke.confait@gmail.com',
    'version' : '1',
    'install_requires' : ['nose'],
    'packages' : ['RSA'],
    'scripts' : [],
    'name' : 'RSA'
    
}

setup(**config)
