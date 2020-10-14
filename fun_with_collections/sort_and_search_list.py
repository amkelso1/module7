"""
Author: Alex Kelso
Date:10/13/2020

program:sort_and_search_list.py
purpose:
"""

mock_list = [7, 2, 6]
print('Unsorted list: ', mock_list)


def search_list():
    try:
        print('index number', mock_list.index(int(input())))  # no use is needed outside of an output
    except ValueError:
        print('-1')


def sort_list():
    mock_list.sort()
    return mock_list  # return for use in other functions if needed


def get_input():
    u_input = input("give me a number: ")
    return u_input


if __name__ == '__main__':
    print('Search Unsorted list: ')
    print(search_list())

    print('Sorted List: ', sort_list())

    print('Search sorted List: ')
    print(search_list())
