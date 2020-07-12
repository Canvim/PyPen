from pyperlib import __version__

import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    setup_requires=["pbr"],
    pbr=True
)
