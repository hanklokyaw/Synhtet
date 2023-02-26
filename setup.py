from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'A templates module for business analytics peers'
LONG_DESCRIPTION = 'A templates module for business analytics peers. The structures and'\
                   'complete script of each analysis models for machine learning is provided.'

# Setting up
setup(
    name="Synhtet",
    version=VERSION,
    author="Htet Aung Kyaw",
    author_email="<hank.lo.kyaw@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['seaborn', 'matplotlib', 'sklearn', 'numpy'],
    keywords=['python', 'business analysis', 'templates', 'MBAN', 'syntax', 'example scripts'],
    classifiers=[
        "Development Status :: Testing(Best)",
        "Intended Audience :: MBAN Peers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
