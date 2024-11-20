
# cli argument / syntax

from os.path import basename
from sys import exit


def syntax(arguments):

    my_name   = basename(arguments.pop(0))

    my_syntax = f'syntax: {my_name} <profile>'

    if len(arguments) != 1: exit(my_syntax)

    return str(arguments[0]).lower()
