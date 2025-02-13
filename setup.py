from setuptools import setup
from sys import platform

from getgit.config import PROG_NAME, PROG_VERS


requirements = ['bs4', 'pyyaml', 'requests']
if platform == 'linux':
    requirements.append('simple-term-menu')


setup(
    name=PROG_NAME,
    version='0.1.8',
    description='Cloning repositories of user',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='GPL3',
    url='https://github.com/kra53n/getgit',
    author='Gregory Bakhtin',
    author_email='greasha46@gmail.com',
    install_requires=requirements,
    packages=['getgit'],
    package_data={'': ['config/*.yaml']},
    entry_points={
        "console_scripts":
            ["getgit = getgit.main:main"]
    },
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Version Control",
        "Topic :: Software Development :: Version Control :: Git ",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Console",
        "Environment :: Console :: CURSES",
    ],
)
