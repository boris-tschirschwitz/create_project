
import argparse
import create_project

parser = argparse.ArgumentParser(description="Create a Python project skeleton.")
parser.add_argument('projectname', type=str, help='The project name.')
parser.add_argument('-k', '--kaggle', nargs='?',
                    default=argparse.SUPPRESS,
                    help='Download kaggle data for competition "KAGGLE". If "KAGGLE" is empty, projectname is used.')

args = vars(parser.parse_args())

if  'kaggle' in args and args['kaggle'] == None:
    args['kaggle'] = args['projectname']

create_project.create_project(**args)
