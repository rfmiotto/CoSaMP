from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent.parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Python implementation of the CoSaMP algorithm'

# Setting up
setup(
    name="cosamp",
    version=VERSION,
    author="Renato Fuzaro Miotto",
    author_email="<renato.fmiotto@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    # packages=find_packages(),
    packages=['cosamp'],
    package_dir={'':'src'},
    install_requires=['numpy'],
    keywords=['python', 'sparse signal', 'cosamp'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)