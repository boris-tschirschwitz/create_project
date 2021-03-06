from os import path, mkdir
from shutil import copy


def create_project(projectname, kaggle=None):
    """
    Create a project folder skeleton named 'name'.

    1. Create a Readme.md with the project name as title.
    2. Copy a basic Makefile and gitignore into the folder.
    3. Create a requirements.txt.
    If 'kaggle' is provided, download data for Kaggle competition 'kaggle'.

    :param projectname: The project name.
    :param kaggle: The competition name.
    """

    create_folder(projectname)
    create_readme(projectname)
    copy_makefile(projectname, kaggle)
    copy_gitignore(projectname)
    create_requirements(projectname, kaggle)


def create_folder(name):
    mkdir(name)


def create_readme(name):
    with open(path.join(name, 'Readme.md'), "w") as targetfile:
        readmetext = '# ' + name + '\n'
        targetfile.write(readmetext)

def copy_makefile(name, kaggle):
    makefile_path = path.join(path.dirname(__file__), 'Makefile')
    if kaggle == None:
        copy(makefile_path, name)
    else:
        kaggle_path = path.join(path.dirname(__file__), 'Makefile_kaggle')
        with open(makefile_path) as makefile:
            with open(kaggle_path) as kagglefile:
                with open(path.join(name, 'Makefile'), "w") as targetfile:
                    makefiletext = makefile.read().replace('all: ', 'all: kaggle ')
                    kaggletext = kagglefile.read().replace('kagglename', kaggle)
                    fullmakefile = makefiletext + '\n' + kaggletext
                    targetfile.write(fullmakefile)


def copy_gitignore(name):
    gitignore_path = path.join(path.dirname(__file__), '.gitignore')
    copy(gitignore_path, name)


def create_requirements(name, kaggle):
    requirementstext = ""
    if kaggle != None:
        requirementstext = requirementstext + "kaggle\n"

    with open(path.join(name, 'requirements.txt'), "w") as targetfile:
        targetfile.write(requirementstext)
