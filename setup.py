from setuptools import setup
from sys import platform


requirements = ["bs4", "pyyaml", "requests"]
if platform == "linux":
    requirements.append("simple-term-menu")

setup(
    name="getgit",
    version="0.1.1",
    description="Cloning repositories of user",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="GPL3",
    url="https://github.com/Krai53n/getgit",
    author="Gregory Bakhtin",
    author_email="greasha46@gmail.com",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        "console_scripts":
            ["getgit = getgit.cli:main"]
    }
)
