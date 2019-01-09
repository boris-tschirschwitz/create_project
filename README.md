# create_project

```
This follows the project structure of "Cookiecutter Data Science".

Example: Set up a project folder for the "titanic" Kaggle competition.
(If you have already joined the competition at Kaggle.)

$ python3 create_project titanic -k
$ cd titanic
$ make

Now the raw Kaggle data can be found in 'data/raw'.
Switch to the project's virtual environment with
$ source activate.

You'll want to add more Python packages to your project
by adjusting 'requirements.txt'. Then call make again to
run pip.

The idea now is to next add new targets to the Makefile
to process the raw data, etc.

To remove all processed data call:
$ make clean 

Help:

$ python3 create_project -h
usage: python3 create_project [-h] projectname [-k [KAGGLE]]

Create a Python project skeleton.

positional arguments:
  projectname           The project name.

optional arguments:
  -h, --help            show this help message and exit
  -k [KAGGLE], --kaggle [KAGGLE]
                        Download kaggle data for competition "KAGGLE". If
                        "KAGGLE" is empty, projectname is used.
```                        