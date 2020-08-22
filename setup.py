from setuptools import setup, find_packages
import os, physics3d

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "physics3d",
    version = physics3d.__version__,
    author = "Ray Chen",
    author_email = "tankimarshal2@gmail.com",
    description = "3d phyics engine based on Pymunk",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github/rayzchen/physics3d",
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    install_requires = [
        
    ],
    python_requires = '>=3.7',
)