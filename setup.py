try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Simple RSA encryption implementation",
    "author": "Luke Confait",
    "url": "https://github.com/LukeConfait/RSA_Encryption",
    "download_url": "Where to download it.",
    "author_email": "luke.confait@gmail.com",
    "version": "2",
    "install_requires": ["nose", "random"],
    "packages": ["RSA"],
    "scripts": [],
    "name": "rsa_lukec",
}

setup(**config)
