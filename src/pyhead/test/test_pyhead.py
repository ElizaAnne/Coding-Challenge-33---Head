# /tests/test_head.py

import  argparse
import  contextlib
import  io
import  unittest
from    unittest.mock import patch

from    ..pyhead import PyHead


class TestHead(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestHead, self).__init__(*args, **kwargs)  
        self.file_dir = 'src/files/' 

    @patch('builtins.input', side_effect=['input_line'] * 10)
    def test_max_10_lines_input(self, mock_input):
        pyhead_instance = PyHead()  # No file_path provided
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            pyhead_instance.display_head()
        output_str = output.getvalue()
        
        # Verify 10 lines outputted without a file path
        expected_output = '\n'.join(['input_line'] * 10) + '\n'
        self.assertEqual(output_str, expected_output)
        
    def test_filename_arg_provided(self):
        file_path = self.file_dir + 'text.txt'

        with patch('sys.argv', ['pyhead.py', file_path]):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                pyhead_instance = PyHead(file_path) 
                pyhead_instance.display_head()
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
        output_without_bom = output.lstrip('\ufeff')     
        self.assertEqual(text, output_without_bom)
    
    def test_custom_bytes_arg(self):
        # Simulate command-line arguments
        with patch('sys.argv', ['pyhead.py', self.file_dir + 'text.txt', '--bytes', '50']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                # Run PyHead with the provided arguments
                pyhead_instance = PyHead(self.file_dir + 'text.txt', bytes=50)  # Pass file_path and bytes explicitly
                pyhead_instance.display_head()

                output = mock_stdout.getvalue()

                # Simulate reading the first 50 bytes of the file
                with open(self.file_dir + 'text.txt', 'r') as file:
                    expected_output = file.read(50)

                self.assertEqual(expected_output, output)

    def test_custom_lines_arg(self):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(filepath='../files/text.txt', lines=50)):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                pyhead_instance = PyHead()
                output = mock_stdout.getvalue()

                expected_output = """The Project Gutenberg eBook of The Art of War
    
                This ebook is for the use of anyone anywhere in the United States and
                most other parts of the world at no cost and with almost no restrictions
                whatsoever. You may copy it, give it away or re-use it under the terms
                of the Project Gutenberg License included with this ebook or online
                at www.gutenberg.org. If you are not located in the United States,
                you will have to check the laws of the country where you are located
                before using this eBook.

                Title: The Art of War


                Author: active 6th century B.C. Sunzi

                Translator: Lionel Giles

                Release date: May 1, 1994 [eBook #132]
                                Most recently updated: October 16, 2021

                Language: English

                Original publication: , 1910


                *** START OF THE PROJECT GUTENBERG EBOOK THE ART OF WAR ***



                Sun Tzŭ
                on
                The Art of War

                THE OLDEST MILITARY TREATISE IN THE WORLD
                Translated from the Chinese with Introduction and Critical Notes

                BY
                LIONEL GILES, M.A.

                Assistant in the Department of Oriental Printed Books and MSS.
                in the British Museum




                1910



                To my brother"""

                self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()