# pyhead.py

import sys

class PyHead:
    def __init__(self, file_path, num_lines=10):
        self.file_path = file_path
        self.num_lines = num_lines

    def display_head(self):
        with open(self.file_path, 'r') as file:
            for _ in range(self.num_lines):
                line = file.readline().rstrip()
                if not line:
                    break  # eof 
                print(line)

if __name__ == "__main__":
    # check if filename provided as argument
    if len(sys.argv) != 2:
        print("Usage: python pyhead.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    py_head = PyHead(file_path)
    py_head.display_head()