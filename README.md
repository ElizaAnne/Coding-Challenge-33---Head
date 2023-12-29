# Coding-Challenge-33---Head

This challenge is to build your own version of the Unix command line tool head, see links below for details. 

[Coding Challenge](https://codingchallenges.fyi/challenges/challenge-head/)

[Head - Ubuntu Man Page](https://manpages.ubuntu.com/manpages/impish/en/man1/head.1.html)

# Usage

This repo uses a Makefile, to run the tool type the command in the terminal

```bash
make pyhead
```
This will run the tool on the default file at src/files/text.txt.

Or run the command (without using Makefile):

```bash
python src/pyhead/pyhead.py src/files/text.txt 
```

To run the tests, run the command:

```bash
make test
```