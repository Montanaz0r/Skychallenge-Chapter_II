import re


def sum_the_numbers(filename):
    """
    A function that sum up all the numbers encountered in the file
    :param filename: name of the file (str)
    :return: sum of all numbers (int)
    """

    with open(f'{filename}.txt', 'r') as file:
        data = file.read()
    results = re.findall(r'(-?\d+)', data)   # using REGEX pattern to detect numbers
    sum_of_all_numbers = sum([int(number) for number in results])
    print(f'Sum of all numbers in the document is equal to: {sum_of_all_numbers}')
    return sum_of_all_numbers


if __name__ == '__main__':
    sum_the_numbers('json_data')
