# scourgify
import sys
import csv

def main():
    check_args()
    # load students into memory
    student_table = []
    # read
    try:
        with open(sys.argv[1], "r",newline='') as before_csv:
            reader = csv.reader(before_csv)
            for row in reader:
                student_table.append(row)
    except:
        sys.exit(f"Could not read {sys.argv[1]}")
    # write
    try:
        with open(sys.argv[2], "w", newline='') as after_csv:
            writer = csv.writer(after_csv)
            writer.writerow(['first', 'last', 'house'])
            for i in range(len(student_table)-1):
                this_row = student_table[i+1]
                name = this_row[0].split(",")
                new_row = [name[1].strip(), name[0].strip(), this_row[1].strip()]
                writer.writerow(new_row)
    except:
        raise
    sys.exit()

def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()