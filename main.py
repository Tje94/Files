__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile


def clean_cache():
    os.chdir('C:\\Users\\tsdri\\Winc\\files')
    if os.path.exists('cache'):
        shutil.rmtree('cache')
    os.makedirs('cache')


def cache_zip(zip_file_path, cache_path):
    with ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(cache_path)


def cached_files():
    list_cached_files = []
    absolute_path = os.path.abspath('C:\\Users\\tsdri\\Winc\\files\\cache')
    dir_cached_files = os.listdir(absolute_path)
    for file in dir_cached_files:
        list_cached_files.append(os.path.join(absolute_path, file))
    return list_cached_files


list_cached_files = cached_files()


def find_password(file_list):
    for file in file_list:
        with open(file, 'r') as details:
            text = details.readlines()
            for line in text:
                if 'password' in line:
                    password_in_list = line[line.find(' ')+1:line.find('\\n')]
    return password_in_list  # correct_horse_battery_staple komt er uit met print


if __name__ == "__main__":
    clean_cache()
    cache_zip('C:\\Users\\tsdri\\Winc\\files\\data.zip', 'C:\\Users\\tsdri\\Winc\\files\\cache')
    cached_files()
    find_password(list_cached_files)
