import os
from datetime import datetime

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime('%d %b %Y %H %M %S')
    return formatted_date

def display_cwd():
    cwd = os.getcwd()
    print(f'Print the current directory: {cwd}')

def up_one_dir():
    os.chdir('..')


def display_files():
    entries = os.scandir()
    for entry in entries:
        info = entry.stat()
        print(f'{entry.name} Creation data: {info.st_blksize}')


def display_directories(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_dir():
            print(f'Directory name is: {entry.name}')


def diplay_files(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_file():
            print(f'File name is: {entry.name}')

display_cwd()
# up_one_dir()
# display_cwd()
# up_one_dir()
# up_one_dir()
# up_one_dir()
# display_cwd()
# display_files()
display_directories('./')
# diplay_files('./')



