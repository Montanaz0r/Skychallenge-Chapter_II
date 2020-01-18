def duplicates_checker(list_of_elements):
    """
    Helper function that checks if there are duplicates in the list.
    :param list_of_elements: python list
    :return: boolean value - False if no duplicates detected, True otherwise
    """
    if len(list_of_elements) == len(set(list_of_elements)):
        return False
    else:
        return True


def valid_skyphrases_counter(filename):
    """
    The function that checks each line of data stored in .txt file for duplicates.
    :param filename: full name (str) of .txt file that has to be checked
    :return: number of lines (int) that do not contain any duplicates
    """
    with open(f'{filename}.txt', 'r') as file:
        data_doc = file.readlines()

    valid_counter = 0
    for line in data_doc:
        listed_line = line.split()
        duplicate = duplicates_checker(listed_line)
        if not duplicate:
            valid_counter += 1

    print(f'The number of valid skyphrases is: {valid_counter}.')
    return valid_counter


if __name__ == '__main__':
    valid_skyphrases_counter('skyphrases_data')


