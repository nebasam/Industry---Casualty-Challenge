import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Causalty",
    version="0.01",
    description="causualty model for breast cancer",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nebasam/Industry---Casualty-Challenge",
    author="Nebiyu Samuel",
    author_email="neba.samuel17@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["package"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "Causualty=package.exploration:main",
        ]
    },
)