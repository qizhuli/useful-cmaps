from setuptools import find_packages
from setuptools import setup

requirements = [
    "numpy",
    "matplotlib",
]

setup(
    name="useful_cmaps",
    version="0.1",
    author="qizhuli",
    url="https://github.com/qizhuli/useful-cmaps",
    description="Handy tool to obtain useful cmaps",
    packages=find_packages(),
    install_requires=requirements,
)
