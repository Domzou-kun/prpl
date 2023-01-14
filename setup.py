from setuptools import setup, find_packages

""" long descriptions for readme.md """
readme_path = "readme.md"
with open(readme_path, encoding="utf-8") as readme_file:
    long_descriptions = readme_file.read()

""" version for version.txt """
version_path = "version.txt"
with open(version_path, encoding="utf-8") as version_file:
    _version = version_file.read()


""" setup """
setup(
    name="progress parallel",
    version=_version,
    description="multi threading progress bar",
    long_description=long_descriptions,
    long_description_content_type='text/markdown',
    url="https://github.com/Domzou-kun/prpl",
    download_url="https://github.com/Domzou-kun/prpl",
    author="Domzou",
    classifiers=[
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Packaging"
    ],
    keywords="Python python progress multi thread threading",
    license="MIT"
)

