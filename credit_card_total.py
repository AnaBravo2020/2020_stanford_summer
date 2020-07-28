"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill1.txt'


def main():
    data = dict()
    file = open(INPUT_FILE, 'r')

    for line in file:
        line = line.strip("\n")
        start = line.find("[")
        end = line.find("]")
        store = line[start+1: end]
        start = line.find("$")
        expense = float(line[start+1:])
        if store in data.keys():
            data[store] = data[store] + expense
        else:
            data[store] = expense

    for store in data.keys():
        print(store + ": $" + str(data[store]))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
