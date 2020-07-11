import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="pyperlib",
    version="0.0.10",
    author="ErikWDev",
    author_email="erikwdev@gmail.com",
    description="A blank paper for your creative adventures in Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Canvim/Pyper",
    packages=setuptools.find_packages(),
    install_requires=[
        ""
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    license="MIT"
)
