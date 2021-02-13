from setuptools import setup, find_packages


from sys import platform
requirements = ["bs4"]
if platform == "linux":
    requirements.append("simple-term-menu")


setup(
    name="getgit",
    version="0.0.1",
    description="Clone repositoryies and give information about them",
    packages=find_pachages(),
    url="https://github.com/Krai53n/getgit",
    author="Gregory Bakhtin",
    author_email="greasha46@gmail.com",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "getgit = getgit.cli:main"
        ]
    }
)