import os
from os import walk
from os.path import exists


def empty_the_output_file(file_path):
    if exists(file_path):
        os.remove(file_path)


def write_into_the_output_file(file_path, content):
    with open(file_path, 'a') as output_file:
        output_file.write(content + '\n')


# target directory
# --------------------------------------------------------------------
current_folder = 'D:\\test'


# the output file
# --------------------------------------------------------------------
generated_file_path = './generated_file_tree.txt'
empty_the_output_file(generated_file_path)


# the `walk` loop
# --------------------------------------------------------------------
for (dir_path, dir_names, file_names) in walk(current_folder):

    write_into_the_output_file(generated_file_path, f'Directory: {dir_path}')
    for directory in dir_names:
        write_into_the_output_file(generated_file_path, f'a directory: {directory}')

    for file in file_names:
        write_into_the_output_file(generated_file_path, f'a file: {file}')

    write_into_the_output_file(generated_file_path, '\n')
