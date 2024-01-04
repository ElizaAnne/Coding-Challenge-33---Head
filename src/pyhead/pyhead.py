# pyhead.py

import argparse

class PyHead:
    def __init__(self, file_path=None, num_lines=10, bytes=0):
        self.file_path  = file_path
        self.num_lines  = num_lines
        self.bytes      = 0

    def display_head(self):
        if self.file_path:
            with open(self.file_path, 'r') as file:
                for _ in range(self.num_lines):
                    line = file.readline()
                    if not line:
                        break  # eof
                    print(line.strip())
        else:
            # This part is for the default behavior of outputting input
            for _ in range(self.num_lines):
                user_input = input() 
                print(user_input)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display the beginning of a file or user input.')
    parser.add_argument('file_path', nargs='?', default=None, help='Path to the file')
    parser.add_argument('--num_lines', type=int, default=10, help='Number of lines to display')
    parser.add_argument('--bytes', type=int, default=0, help='Number of bytes to display')
    args = parser.parse_args()

    py_head = PyHead(args.file_path, args.num_lines, args.bytes)
    py_head.display_head()