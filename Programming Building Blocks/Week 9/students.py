import csv

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    student_dict = read_dict("students.csv", I_NUMBER_INDEX)

    id = input("Enter a student ID: ")
    if id in student_dict:
        value = student_dict[id]
        name = value[NAME_INDEX]
        print(name)
    else:
        print("No such student")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}
    with open(filename, 'rt') as students_file:
        reader = csv.reader(students_file)
        next(reader)
        for row_list in reader:
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            student_dict[key] = row_list

    return student_dict

if __name__ == "__main__":
    main()
