import csv
import sys
import tabulate

def main():
    try:
        if check_usage(len(sys.argv), sys.argv[1]):
            sys.exit(1)
    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)
    table_array = []
    keys = []
    try:
        with open(sys.argv[1], "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                # getting headers
               if not keys:
                   # print("Getting keys")
                   keys = list(line.keys())
                   table_array.append(keys)
                # getting row
               row_array = []
               for i in range(len(line)):
                   row_array.append(line[keys[i]])
               table_array.append(row_array)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    print(tabulate.tabulate(table_array[1:], headers=table_array[0], tablefmt="grid"))
    sys.exit()

def check_usage(arg_num, file_name):
    if arg_num < 2:
        print("Too few command-line arguments")
        return True
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        return True
    elif file_name[-4:] != '.csv' or sys.argv[-1] == '..':
        print("Not a CSV file")
        return True
    return False

if __name__ == "__main__":
    main()