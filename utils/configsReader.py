import os
from typing import Union

import yaml

from .objects import DictOperating


def loadConfigInYAML(path: str) -> dict:
    """Read configuration file in `YAML` format

    Parameters
    ----------
    path : str
        file path

    Returns
    -------
    dict
        Reading results
    """
    with open(path, "rb") as f:
        ymlLoad = yaml.safe_load(f)
    return ymlLoad if type(ymlLoad) == dict else dict()


def filenameQuickChange(file: str, name: str) -> str:
    path, _ = os.path.split(file)
    return os.path.join(path, name)


def touchFile(path: str, newContent: Union[str, bytes] = None) -> None:
    if not os.path.isfile(path):
        if type(newContent) == bytes:
            with open(path, "wb") as f:
                f.write(newContent)
        elif type(newContent) == str:
            with open(path, "wt", encoding="utf-8") as f:
                f.write(newContent)
    return path


def copyFileInText(originPath: str, targetPath: str, encoding: str = "utf-8") -> int:
    """Copy a file in text encoding

    Parameters
    ----------
    originPath : str
        Source file path
    targetPath : str
        Destination file path
    encoding : str, optional
        encoding, by default 'utf-8'

    Returns
    -------
    int
        Number of bytes written
    """
    with open(originPath, "rt", encoding=encoding) as origin, open(
        targetPath, "wt", encoding=encoding
    ) as target:
        totalWrite: int = target.write(origin.read())
    return totalWrite


touch = touchFile
filePath = filenameQuickChange
configLoad = loadConfigInYAML


class configsReader:
    """Read setting object"""

    def __init__(self, configDir: str, defaultDir: str):
        """__init__ [summary]

        Parameters
        ----------
        configDir : str
            Configuration file directory (must exist)
        defaultDir : str
            Default configuration file directory.
            Called back when settings not found in the configuration file are taken.
        """
        assert os.path.isfile(configDir)
        assert os.path.isfile(defaultDir)
        self.__config = DictOperating.enhance(loadConfigInYAML(configDir))
        self.__default = DictOperating.enhance(loadConfigInYAML(defaultDir))

    def __getattr__(self, key):
        return self.__config.get(key, self.__default[key])

    def __dict__(self):
        return {
            key: DictOperating.weaken(self.__getattr__(key)) for key in self.__default
        }
