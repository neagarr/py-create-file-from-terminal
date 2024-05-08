import os
import sys
import datetime

arg_list = [arg for arg in sys.argv]


def create_directory(directory: str) -> None:
    full_path = f"{os.getcwd()}/{directory}"
    if not os.path.exists(full_path):
        os.makedirs(full_path)


def create_file(name_of_file: str) -> None:
    with open(name_of_file, "a") as new_file:
        line_number = 1
        new_file.write(
            f"\n{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            new_file.write(f"{line_number} {line}\n")
            line_number += 1


if "-d" in arg_list and "-f" in arg_list:

    if arg_list.index("-d") < arg_list.index("-f"):
        path = ("/".join(
            arg for arg in
            arg_list[arg_list.index("-d") + 1:arg_list.index("-f")]
        ))
        file_name = f"{os.getcwd()}/{path}/{arg_list[-1]}"

    else:
        path = "/".join(arg for arg in arg_list[arg_list.index("-d") + 1::])
        file_name = (
            f"{os.getcwd()}/{path}/{arg_list[arg_list.index('-f') + 1]}"
        )

    create_directory(path)
    create_file(file_name)


elif "-d" in arg_list:
    path = "/".join(arg for arg in arg_list[arg_list.index("-d") + 1::])
    create_directory(path)


elif "-f" in arg_list:
    file_name = f"{os.getcwd()}/{arg_list[-1]}"
    create_file(file_name)
