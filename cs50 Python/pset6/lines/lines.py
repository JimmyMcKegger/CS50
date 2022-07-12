# reads a file and outputs the number of lines of code, omiting comments and blank lines
import sys

def count_lines(file_name):
    count = 0
    try:
        with open(file_name) as f:
            for line in f:
                if line.lstrip().startswith('#') or line.isspace():
                    continue
                else:
                    count += 1
        return count
    except FileNotFoundError:
        raise

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1][-3:] != '.py' or sys.argv[-1] == '..':
        print("Not a Python file")
        sys.exit(1)
    else:
        try:
            file_name = sys.argv[1]
            num = count_lines(file_name)
            print(num)
            sys.exit(0)
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
        except IsADirectoryError:
            print("Not a Python file")
            sys.exit(1)

if __name__ == "__main__":
    main()