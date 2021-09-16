
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pysocksproto",
	version="0.1.0",
	author="Daniil Tumanov",
	author_email="fkohs@inbox.ru",
	description="Customizable python module for create your own programs on SOCKS protocol ",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/fkohs/py_socksproto",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.6",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)