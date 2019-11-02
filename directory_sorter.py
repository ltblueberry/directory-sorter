#!/usr/bin/python

import argparse
import os
import sys
import re


class printColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


class messages:
    NONE_DIR = "a directory is not defined"
    DIR_NOT_FOUND = "The directory {} was not found"
    IS_NOT_DIR = "{} is not a directory"
    DONE = "done"


need_print = False


def print_if_needed(string):
    if need_print:
        print string


def main(directory):
    if directory is None:
        exit_message = messages.NONE_DIR
        print_if_needed("-d, --directory     " + printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    if os.path.exists(directory) == False:
        exit_message = messages.DIR_NOT_FOUND.format(
            os.path.abspath(directory))
        print_if_needed(printColor.RED + exit_message + printColor.END)
        return exit_message

    if os.path.isdir(directory) == False:
        exit_message = messages.IS_NOT_DIR.format(
            os.path.abspath(directory))
        print_if_needed(printColor.RED + exit_message + printColor.END)
        return exit_message

    return messages.DONE


if __name__ == "__main__":
    need_print = True
    parser = argparse.ArgumentParser(
        description='Move all files from the specified directory to the appropriate created subfolder by type.')

    parser.add_argument('-d', '--directory', metavar='',
                        help='the directory that needs file sorting')

    args = parser.parse_args()

    directory = args.directory

    main(directory)
