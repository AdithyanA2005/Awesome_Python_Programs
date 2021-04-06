import os


def check_word(word, filename, folder):
    with open(f"{folder}/{filename}", "r") as f:  # This will open the file
        file_content = f.read()  # This will get us the file contents

        if word.upper() in file_content.upper():  # If the word is in the file
            return True   # Return True

        else:  # If the word is not in the file
            return False  # Return False


def main(word, folder):
    file_list = os.listdir(folder)

    for files in file_list:  # For each files in the folder
        if files.endswith('txt'):  # We will only check the '.txt' files for the word
            print("\n")
            print(f"Checking for {word} in {files}")

            # Now we will check for the word in the filename
            word_flag = check_word(word, files, folder)

            if word_flag:
                print(f"{word} was found in {files}")

            else:
                print(f"{word} was not Found in {files}")


if __name__ == "__main__":
    word = 'binod'
    folder = 'custom_files'
    main(word, folder)
