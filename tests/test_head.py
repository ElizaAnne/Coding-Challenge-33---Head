# /tests/test_head.py

import  argparse
import  io
import  unittest
from    unittest.mock import patch
#from head import main

class TestHead(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(filepath='../files/text.txt'))
    def test_filename_argument_provided(self, mock_parse_args):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            #main()
            output = mock_stdout.getvalue()
        
        text = """The Project Gutenberg eBook of The Art of War
    
This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

"""
        self.assertEqual(text, output)


if __name__ == '__main__':
    unittest.main()