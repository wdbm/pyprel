#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import setuptools

def main():

    setuptools.setup(
        name             = "pyprel",
        version          = "2017.02.16.1353",
        description      = "Python print elegant",
        long_description = long_description(),
        url              = "https://github.com/wdbm/pyprel",
        author           = "Will Breaden Madden",
        author_email     = "wbm@protonmail.ch",
        license          = "GPLv3",
        py_modules       = [
                           "pyprel"
                           ],
        install_requires = [
                           "Image",
                           "numpy",
                           "pyfiglet",
                           "shijian"
                           ],
        entry_points     = """
            [console_scripts]
            pyprel = pyprel:pyprel
        """
    )

def long_description(
    filename = "README.md"
    ):

    if os.path.isfile(os.path.expandvars(filename)):
        try:
            import pypandoc
            long_description = pypandoc.convert_file(filename, "rst")
        except ImportError:
            long_description = open(filename).read()
    else:
        long_description = ""
    return long_description

if __name__ == "__main__":
    main()
