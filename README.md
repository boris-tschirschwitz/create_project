# create_project

## Usage

This follows the project structure of
[Cookiecutter Data Science -- Directory Structure](https://drivendata.github.io/cookiecutter-data-science/#directory-structure)

Example: Set up a project folder for the "titanic" Kaggle competition.
(If you have already joined the competition at Kaggle and set up a local kaggle.json, see [Create kaggle.json](#create-kagglejson).)

```bash
python3 create_project titanic -k
cd titanic
make
```

Now the raw Kaggle data can be found in 'data/raw'.
Switch to the project's virtual environment with

```bash
source activate.
```

You'll want to add more Python packages to your project
by adjusting 'requirements.txt'. Then call make again to
run pip.

The idea now is to next add new targets to the Makefile
to process the raw data, etc.

To remove all processed data call:

```bash
make clean
```

## Create kaggle.json

The `kaggle` command uses the local file `~/.kaggle/kaggle.json` for authentication.

To create this file log into your account at [kaggle](https://www.kaggle.com),
go to "My account" and  Click on "Create new API Token".
This will download the file 'kaggle.json'.

Copy this file to `~/.kaggle/kaggle.json`.

## Help:

```bash
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
