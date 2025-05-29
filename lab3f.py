#!/usr/bin/env python3
# Author ID: rbhandari17@myseneca.ca

# Global list
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends a new item that is one more than the last item in the list
    last_item = ordered_list[-1]
    ordered_list.append(last_item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes each item in items_to_remove from the ordered_list if it exists
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)  # [1, 2, 3, 4, 5]
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8]
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)  # [2, 3, 4, 7, 8]
