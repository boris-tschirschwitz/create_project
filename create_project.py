from os import path, mkdir
from shutil import copy


def create_project(name):
    """
    Create a project folder skeleton named 'name'.

    Copy a basic Makefile and gitignore into the folder.

    :param name: The project name.
    """

    create_folder(name)
    copy_makefile(name)
    copy_gitignore(name)


def create_folder(name):
    mkdir(name)


def copy_makefile(name):
    makefile_path = path.join(path.dirname(__file__), 'Makefile')
    copy(makefile_path, name)

def copy_gitignore(name):
    gitignore_path = path.join(path.dirname(__file__), '.gitignore')
    copy(gitignore_path, name)


if __name__ == "__main__":
    import sys

    create_project(sys.argv[1])
