from setuptools import setup
from sys import platform

from getgit.constants import PROG_NAME, PROG_VERS


requirements = ['bs4', 'pyyaml', 'requests']
if platform == 'linux':
    requirements.append('simple-term-menu')


setup(
    name=PROG_NAME,
    version=PROG_VERS,
    description='Cloning repositories of user',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='GPL3',
    url='https://github.com/kra53n/getgit',
    author='Gregory Bakhtin',
    author_email='greasha46@gmail.com',
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=['getgit'],
    package_data={'': ['config/*.yaml']},
    entry_points={
        "console_scripts":
            ["getgit = getgit.main:main"]
    }
)
