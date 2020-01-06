
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.
import tabulate

def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for item in inventory:
        print(f'{item}: {inventory.get(item)}')


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    pass


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    pass


def print_table(inventory, order='empty'):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    dash = '-' * 17
    pipe = '|'
    first_column = 'item name'
    second_column = 'count'
    sorted_inventory = {}

    ''' 
    sort by value - first swap the key value pair
    then convert tuple to dict again
    '''
    if order == 'count,asc':
        temp_inventory_tuple = sorted(inventory.items(), key=lambda x: x[1])
        for item in temp_inventory_tuple:
            sorted_inventory[item[0]] = item[1]

    elif order == 'count,desc':
        temp_inventory_tuple = sorted(inventory.items(), reverse=True, key=lambda x: x[1])
        for item in temp_inventory_tuple:
            sorted_inventory[item[0]] = item[1]

    else:
        sorted_inventory = inventory

    print(dash)
    print('{:>9s} {} {:>5s}'.format(first_column, pipe, second_column))
    print(dash)

    for item in sorted_inventory:
        print('{:>9s} {} {:>5s}'.format(item, pipe, str(sorted_inventory.get(item))))

    print(dash)


def import_inventory(inventory, filename='test_inventory.csv'):
    """Import new inventory items from a CSV file."""
    temp_list_of_items = []
    try:
        with open(filename, 'r') as csv_file:
            for item in csv_file:
                temp_list_of_items.append(item.split(','))

        for i in temp_list_of_items[0]:
            inventory[i] = temp_list_of_items[0].count(i)

        return inventory

    except (FileNotFoundError, IOError):
        print(f"File '{filename}' not found!")



def export_inventory(inventory, filename='test_inventory.csv'):
    """Export the inventory into a CSV file."""

    inventory_list = []
    for item in inventory:
        occurrences = inventory[item]
        inventory_list.extend([item for i in range(0, occurrences)])

    number_of_items = len(inventory_list)
    items_saved = 1

    try:
        with open(filename, 'w') as csv_file:
            for items_to_save in inventory_list:
                csv_file.write(items_to_save + ',') if number_of_items != items_saved else csv_file.write(items_to_save)
                items_saved += 1

    except (PermissionError, IOError):
        print(f"You don't have permission creating file '{filename}'!")


def main():
    #inventory_test = {'cycki': 4}
    inventory = import_inventory({})

    #inventory = {}
    #display_inventory(inventory)

    print_table(inventory)
    print('####################')
    print_table(inventory, 'count,desc')
    print('####################')
    print_table(inventory, 'count,asc')
    print('####################')

    #export_inventory(inventory)


if __name__ == '__main__':
    main()