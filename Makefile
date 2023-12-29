FILE_PATH := src/files/

# Change this to your filename in the /files dir
FILE_NAME := text.txt

ifndef FILE
	FILE := $(FILE_PATH)$(FILE_NAME)
endif

pyhead:
	@echo "Head of file: $(FILE)"
	python src/pyhead/pyhead.py $(FILE)

test:
	pytest src/pyhead/test/