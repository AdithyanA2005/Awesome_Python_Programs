import os
from folder_cleaner.orderer import list_files
from folder_cleaner.orderer import manage
from folder_cleaner.orderer import file_remove
from folder_cleaner.data_set import none_include_files
from folder_cleaner.data_set import file_location
from folder_cleaner.data_set import file_types


if __name__ == '__main__':
    files = os.listdir()
    file_remove(none_include_files, files)
    list_files(files)
    manage(file_location, file_types, files)


