import os
import shutil


def create_project(name):
    """
    Create a folder 'name' and a basic Makefile inside.

    :param name: The project name.
    """

    create_folder(name)
    copy_makefile(name)


def create_folder(name):
    os.mkdir(name)


def copy_makefile(name):
    makefile_path = os.path.join(os.path.dirname(__file__), 'Makefile')
    shutil.copy(makefile_path, name)


if __name__ == "__main__":
    import sys

    create_project(sys.argv[1])
