# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

import csv


# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print("%s %s" % (v, k))
    print("Total number of items: %d" % sum(inventory.values()))
    pass


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for loot in added_items:
        for k in list(inventory.keys()):
            if loot == k:
                inventory[k] += 1
            if loot not in inventory.keys():
                inventory[loot] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):

    l = dict(inventory)
    l.update({"item name": "count"})
    n1 = max(len(str(i)) for i in l.values())
    n2 = max(len(i) for i in l.keys())

    print("Inventory:")
    print("  "+" "*(n1-len("count"))+"count"+"    "+" "*(n2-len("item name"))+"item name")
    print("-"*(n1+n2+6))
    if order == "count,asc":
        c = sorted(inventory.items(), key=lambda x: x[1])
    elif order == "count,desc":
        c = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    else:
        c = list(inventory.items())
    for i in c:
        print("  "+" "*(n1-len(str(i[1])))+str(i[1])+"    "+" "*(n2-len(i[0]))+i[0])
    print("-"*(n1+n2+6))
    print("Total number of items: "+str(sum(inventory.values())))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as im_file:
        im_str = im_file.read()
        im_list = im_str.split(",")
        add_to_inventory(inventory, im_list)
    im_file.closed


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    file = open(filename, "w", newline='')
    writer = csv.writer(file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    data = []
    for k, v in inventory.items():
        data.extend([k] * v)
    writer.writerow(data)
    file.close()


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
display_inventory(inv)
inv = add_to_inventory(inv, dragon_loot)
import_inventory(inv, "import_inventory.csv")
print_table(inv, "count,desc")
export_inventory(inv, "export_iventory.csv")
