import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Annif',
    version='0.23',
    url='https://github.com/NatLibFi/Annif',
    author='Osma Suominen',
    author_email='osma.suominen@helsinki.fi',
    description='Statistical automated subject indexing and classification tool',
    long_description=read('README.md'),
    packages=find_packages(),
    install_requires=[],
    entry_points={'console_scripts': ['annif=annif.cli:cli']}
)
