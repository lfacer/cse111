import csv

PRODUCT_NUMBER_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2
QUANTITY = 1

def main ():

    products_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX, NAME_INDEX, PRICE_INDEX)
    requests_dict = read_dict("requests.csv", PRODUCT_NUMBER_INDEX, QUANTITY)

print()

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    products_dict = {}
    with open(filename, 'rt') as product_file:
        reader = csv.reader(product_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            products_dict[key] = row_list

    requests_dict = {}
    with open(filename, 'rt') as requests_file:
        reader = csv.reader(requests_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            requests_dict[key] = row_list
    
    return products_dict and requests_dict

if __name__ == "__main__":
    main()