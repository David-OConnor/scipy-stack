from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name="scipy-stack",
    version="0.0.1",
    packages=find_packages(),

    install_requires=[],

    author="",
    author_email="",
    url='',
    description="Helper package to install the scipy stack",
    long_description=readme,
    license="Apache 2.0",
    keywords="scipy-stack, scipy, numpy",
)
