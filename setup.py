import codecs
import os

from setuptools import setup, find_packages



HERE = os.path.abspath(os.path.dirname(__file__))

NAME = "Fuzzy_Clustering"
DESCRIPTION = "an implementation of fuzzy clustering algorithms"
VERSION = "1.0.0"

URL = "https://github.com/Sam-damn/Fuzzy-Clustering"
AUTHOR = "Sameh Haidar"
AUTHOR_EMAIL = "samxxhaider@gmail.com"
KEYWORDS = ["fuzzy", "cluster", "fuzzy c means"]


PACKAGES = find_packages(where="src")
INSTALL_REQUIRES = ["numpy>=1.16.4"]


def read(name):
    with codecs.open(os.path.join(HERE, name), "r", "utf-8") as f:
        return f.read()
        

if __name__ == "__main__":

    setup(
          name = NAME,
          description = DESCRIPTION,
          license = "MIT",
          version = VERSION,
          url = URL,
          author = AUTHOR,
          author_email = AUTHOR_EMAIL,
          keywords = KEYWORDS,
          long_description = read("README.md"),
          long_description_content_type = "text/markdown",
          classifiers = [
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",],
          packages = PACKAGES,
          package_dir = {"": "src"},
          install_requires = INSTALL_REQUIRES,
          python_requires = ">=3.6",  
          package_data = {
        "fuzzy_clustering":["data/*.jpeg"]
          },
          include_package_data = True,
          extras_require = {
        "examples":  ["matplotlib","opencv-python","scikit-image","scikit-learn"]})
          
          
          
          