import sys
from pyhead import PyHead

def main():
    # check if filename provided as argument
    if len(sys.argv) != 2:
        print("Usage: python pyhead.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    py_head = PyHead(file_path)
    py_head.display_head()


if __name__ == "__main__":
    main()