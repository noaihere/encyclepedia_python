from setuptools import setup, find_packages

setup(
    name='testproject',
	version='0.1',
	packages= find_packages(exclude=('docs'))
)