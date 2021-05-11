import os


def create_if_not_exist(folder):
    """ This is a function that will create folders if they do not exists """
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folder_name, files):
    """ This fucntion will move files into folders """
    for file in files:
        os.replace(file, f"{folder_name}/{file}")


def file_remove(none_include_list, files):
    for item in none_include_list:
        files.remove(item)


def list_files(files):
    """ This function will show the files and folders in a folder """
    index_no = 0
    print("THESE ARE THE FILES ON THIS FOLDER")

    for file in files:
        index_no = index_no + 1
        print(f"{index_no}-    {file}")
    print("\n")


def arrange(location, extensions, files):
    """ This function will move the specific files fo specific folders """
    create_if_not_exist(location)
    my_files = [file for file in files if os.path.splitext(file)[1].lower() in extensions]
    move(location, my_files)


def manage(file_location, file_types, files):
    """ This function will take different datasets from data_set.py and use arrange function in them """
    no_of_items = 1
    for items in file_location:  # This will calculate the total number of items in the dataset
        no_of_items = no_of_items + 1

    for key in range(1, no_of_items):  # This will arrange the dataset using arrange function
        arrange(file_location[f"ty{key}"], file_types[f"ty{key}"], files)
