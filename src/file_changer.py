"""
Class: CYBR 498

Student: Brevin Wulterin

Purpose:

        This file will read through each .py file in Group2_SlightlyModified_NotHashed and
        make modifications to it in some kind of random sense.
        it iwll add the shake_it_off_lyrics to the file RELATIVE_FILE_PATH
        it will then delete all lines with import and def keywords
        it will then shuffle all of the lines in a random order
        it will also delete a random number of lines (between 1 - 20)

"""
import random
import os

RELATIVE_FILE_PATH = "Group2_SlightlyModified_NotHashed"

shake_it_off_lyrics ="""I stay out too late
Got nothing in my brain
That's what people say, mm-mm
That's what people say, mm-mm
I go on too many dates
But I can't make 'em stay
At least that's what people say, mm-mm
That's what people say, mm-mm
But I keep cruisin'
Can't stop, won't stop movin'
It's like I got this music in my mind
Sayin', "It's gonna be alright"
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
"""

def add_lines(file_path, string_to_add):
    """
    Purpose: This file will write a string of words to the file, file_path

    Parameters: file_path = the relative path to a .py file
                string_to_add = the string, shake_it_off_lyrics, which will be added to the .py file_path variable

    return: None

    """

    with open(file_path, 'a') as py_file:
        py_file.write(string_to_add)


def delete_lines_with_def(file_path):
        """
    Purpose: This function will read a file, delete any lines with the 'def' and 'import' keywords, and shuffle lines.
             It will write the results back to the file

    Parameters: file_path = the relative path to a .py file

    return: None(but it will make in place adjustments to a list and write that list to the file)

    """

    
    # read through each line
    with open(file_path, 'r', encoding = "utf-8") as py_file:
        lines = py_file.readlines()
    # define a new list to keep lines without def
    kept_lines = []

    for line in lines:
        if 'def' not in line and 'import' not in line:
            kept_lines.append(line)
    
    # using the random library to shuffle all lines
    random.shuffle(kept_lines)

    # now this will rewrite the files
    with open(file_path, 'w', encoding= "utf-8") as py_file:
        py_file.writelines(kept_lines)

def delete_random_lines(file_path):
    """
    I basically copy and pasted from the function delete_lines_with_def
    and made necessary adjustments

    Purpose: This function will read a file, delete a random number of lines(between 1 to 20)
             It will write the results back to the file

    Parameters: file_path = the relative path to a .py file

    return: None(but it will make in place adjustments to a list and write that list to the file)
    """
    # read through each line
    with open(file_path, 'r', encoding = "utf-8") as py_file:
        lines = py_file.readlines()

    # variable that will determine how many lines to delte
    num = random.randint(1,20)
    
    kept_lines = []

    for line in lines:
            kept_lines.append(line)
    
    
    # using the random library to suffle the list and delete num amount of liens
    random.shuffle(kept_lines)
    for i in range(num):
        kept_lines.pop()

    # now this will rewrite the files
    with open(file_path, 'w', encoding= "utf-8") as py_file:
        py_file.writelines(kept_lines)

        
# finally I will create a for loop that iterates over each .py file in Group2_SlightlyModified_NotHashed
for file_name in os.listdir(RELATIVE_FILE_PATH):

    # create a random variable to randomized if an above function is called
    ran_num1 = random.randint(1,3)
    ran_num2 = random.randint(1,3)
    
    filepath = os.path.join(RELATIVE_FILE_PATH, file_name)

    # invoke each of these functions on the current file in the for loop
    add_lines(filepath,shake_it_off_lyrics)
    if ran_num1 == 1:
        delete_lines_with_def(filepath)
    if ran_num2 == 2:
        delete_random_lines(filepath)

print("File modfications complete")
