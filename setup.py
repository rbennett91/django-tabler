from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-tabler',
    version='0.0.32',
    description='Django static files & templates for the Tabler dashboard',
    long_description=long_description,
    url='https://github.com/rbennett91/django-tabler',
    author='Ryan Bennett',
    author_email='ryan.bennett@outlook.com',
    packages=[
        'tabler',
    ],
    install_requires=[],
)
