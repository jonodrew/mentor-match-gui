import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mentor-match",
    version="0.1.0",
    description="A graphical interface to the mentor-match package",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Jonathan Kerr",
    author_email="jonathan.drew.kerr@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["app"],
    include_package_data=True,
    install_requires=["mentor-match"],
    setup_requires=["wheel"],
)
