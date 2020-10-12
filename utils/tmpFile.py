#!/bin/env python
# coding=UTF-8
# This is a third-party library from https://github.com/yingyulou/tmpFile
"""
DESCRIPTION

    tmpFile

    A module for creating temporary files and folders.

VERSION

    1.4.0

LATEST UPDATE

    2019.3.4

"""

# Import Python Lib
from os import mkdir, remove
from os.path import abspath, exists, join
from shutil import rmtree
from uuid import uuid4

################################################################################
# Tmp File
################################################################################

TEMP_DIR = "./data/temp"

if not exists(TEMP_DIR):
    mkdir(TEMP_DIR)


class tmpFile(object):
    """
    DESCRIPTION

        Create a tmp file.

    USAGE

        from tmpFile import tmpFile

        with tmpFile() as tmpFileName, open(tmpFileName, 'w') as fo:
            ...

        # File: "tmpFileName" will be deleted automatically (if exist)

    ARGUMENT

        * ext = '', str
            The extension of the tempfile.

        * path = './', str
            The path of the tempfile.
    """

    __slots__ = ("__tmpFileName",)

    def __init__(self, ext=".tmp", path=TEMP_DIR):

        self.__tmpFileName = abspath(join(path, uuid4().hex + ext))

    def __enter__(self):

        return self.__tmpFileName

    def __exit__(self, *exc_info):

        if exists(self.__tmpFileName):
            remove(self.__tmpFileName)


################################################################################
# Tmp Folder
################################################################################


class tmpFolder(object):
    """
    DESCRIPTION

        Create a tmp folder.

    USAGE

        from tmpFile import tmpFolder

        with tmpFolder() as tmpFolderPath:
            ...

        # Folder: "tmpFolderPath" will be deleted automatically (if exist)

    ARGUMENT

        * path = './', str
            The path of the tmp folder.
    """

    __slots__ = ("__tmpFolderName",)

    def __init__(self, path=TEMP_DIR):

        self.__tmpFolderName = abspath(join(path, uuid4().hex))

    def __enter__(self):

        mkdir(self.__tmpFolderName)

        return self.__tmpFolderName

    def __exit__(self, *exc_info):

        if exists(self.__tmpFolderName):
            rmtree(self.__tmpFolderName)
