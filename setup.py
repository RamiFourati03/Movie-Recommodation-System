from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# edit below variables as per your requirements -
PROJECT_SLUG = "Movie-Recommodation-System"
AUTHOR = "RamiFourati03"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit"]

setup(
    name=PROJECT_SLUG,
    version="0.0.1",
    author=AUTHOR,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{PROJECT_SLUG}",
    author_email="ramifourati@ieee.org",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
)
