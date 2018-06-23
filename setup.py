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
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['django', 'tabler', 'dashboard', 'template', 'ui'],
    author='Ryan Bennett',
    author_email='ryan.bennett@outlook.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
