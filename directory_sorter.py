#!/usr/bin/python

import argparse
from os import path, listdir, mkdir
import shutil
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


def get_extension(file):
    return path.splitext(file)[1]


def get_sub_directory_name(extension):
    sub_directory = extension
    if not sub_directory:
        sub_directory = "no_extension"
    else:
        # remove dot
        sub_directory = sub_directory[1:]
    return sub_directory


def main(directory):
    if directory is None:
        exit_message = messages.NONE_DIR
        print_if_needed("-d, --directory     " + printColor.RED +
                        exit_message + printColor.END)
        return exit_message

    if path.exists(directory) == False:
        exit_message = messages.DIR_NOT_FOUND.format(
            path.abspath(directory))
        print_if_needed(printColor.RED + exit_message + printColor.END)
        return exit_message

    if path.isdir(directory) == False:
        exit_message = messages.IS_NOT_DIR.format(
            path.abspath(directory))
        print_if_needed(printColor.RED + exit_message + printColor.END)
        return exit_message

    files = [f for f in listdir(
        directory) if path.isfile(path.join(directory, f))]

    extensions = list(set(map(get_extension, files)))

    for extension in extensions:
        sub_directory_name = get_sub_directory_name(extension)
        sub_directory_path = path.join(directory, sub_directory_name)

        if not path.exists(sub_directory_path):
            mkdir(sub_directory_path)

        matched_files = filter(lambda x: path.splitext(x)[
                               1] == extension, files)

        for matched_file in matched_files:
            source = path.join(directory, matched_file)
            dest = path.join(sub_directory_path, matched_file)
            shutil.move(source, dest)

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
