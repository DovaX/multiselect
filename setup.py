import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='multiselect',
    version='0.1.0',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='A Python package for easy storing and manipulating with data coming from a multiselect dropdown menu',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/multiselect',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          
     ],
    python_requires='>=3.6',
)
    