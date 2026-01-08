import os
import argparse

#Exercise 1
def count_entries(filename: str) -> list[str]:
    """
    It takes a filename as argument
    returns the total number of lines (entries) in the file including empty lines.
    """
    num_lines = 0

    with open(filename, "r") as file_obj:
        lines = file_obj.readlines()

        for l in lines:
            if l in lines:
                num_lines += 1
    return num_lines
    
#Exercise 2
def count_populated_entries(filename: str) -> int:
    """
    It takes a filename as argument
    returns the number of non-empty lines in the file.
    """
    num_populated_lines = 0
    
    with open(filename, "r") as file_obj:
        for l in file_obj:
            if l.strip() != "":
                num_populated_lines +=1

    return num_populated_lines

#Exercise 3 - List unique entries
def list_unique(filename: str) -> set[str]:
    """
    Get a set of unique names from the file
    Clean up White space
    No duplicate names
    """
    unique_names = set()

    with open(filename, "r") as file_obj:
        for l in file_obj:
            if l.strip() != "":
                unique_names.add(l)

    return unique_names

#Exercise 4 - Create a CLI Application
def main() -> None:
    """
    Takes a positional argument filename - the file to process
    Provides four mutually exclusive optional flags:
    -a or --all: Count all lines (including empty lines) using count_entries
    -c or --count: Count non-empty lines only using count_populated_entries
    -u or --unique: List unique entries (unsorted) using list_unique
    -s or --sorted: List unique entries sorted alphabetically (default if no flag specified)
    """

    parser = argparse.ArgumentParser(description='Counting and listing names')

    parser.add_argument('in_string', type=str, help='The string to process')

    operation = parser.add_mutually_exclusive_group()

    operation.add_argument('-a', '--all', action='store_true', 
                      help='Use the count_entries function')
    operation.add_argument('-c', '--count', action='store_true', 
                      help='Use the count_populated_entries function')
    operation.add_argument('-u', '--unique', action='store_true', 
                      help='Use the list_unique function')
    operation.add_argument('-s', '--sorted', action='store_true', 
                      help='Uses the sorted function (default)')
    
    args = parser.parse_args()

    result = None
    
    print(f"Input string: {args.in_string}\n")
    
    if args.all:
        result = count_entries(args.in_string)
        operation_name = "Count all entries"
    elif args.count:
        result = count_populated_entries(args.in_string)
        operation_name = "Count all non-white space entries"
    elif args.unique:
        unique_names = list_unique(args.in_string)
        result = "\n".join(unique_names)
        operation_name = "List all unique names"
    else:
        sorted_names = sorted(list_unique(args.in_string))
        result = "\n".join(sorted_names)
        operation_name = "Sort names alphabetically"

    print(f"Input: '{args.in_string}'")
    print(f"Operation: {operation_name}")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()