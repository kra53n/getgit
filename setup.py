from setuptools import setup, find_packages


from sys import platform
requirements = ["bs4"]
if platform == "linux":
    requirements.append("simple-term-menu")
if platform == "win32":
    requirements.extend(
        [
            "pyyaml",
            "requests",
        ]
    )


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="getgit",
    version="0.0.2",
    description="Cloning repositories of user",
    long_description=long_description,
    license="GPL3",
    packages=find_packages(),
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
