import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="YTchannel",
    version="0.0.8",
    author="Sanjay Developer",
    author_email="sureshsanjay805@gmail.com",
    description="YouTube channel & video details extractor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanjayDevTech/YTchannel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)