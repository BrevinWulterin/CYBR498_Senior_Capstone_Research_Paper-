"""

Class:      CYBR 498

Student:    Brevin Wulterin

This script will create a function that uses the SHA256 algorithm to create a hash digest of all
100 files in "folder passed in as argument". The digest of each hash will be added
to a set.
"""
import os
import hashlib



def hashfunction(target_file):
    """
    Purpose:
    This function will hash the file passed in as an argument

    Parameters:
    target_file = a .py file which will be hashed
    
    return:
    the hash digest
    """
    BUFFER_SIZE = 65536

    # create our hashing algorhim object
    sha256_algo = hashlib.sha256()

    # open the file using a with statement so files automatically close
    with open(target_file, 'rb') as current_file:
        # loop through current_file and store it in a variable called data
        # loop breaks when there is no more data to be read
        while True:
            data = current_file.read(BUFFER_SIZE)

            if not data:
                break
            # invoking the update method on our sha256_algo and passing in the data variable
            sha256_algo.update(data) 
    return sha256_algo.hexdigest()



def folder_iteration(folder_name, output_in_terminal):
    """
    Purpose:
    This function will iterate throguh each individual file in a folder,
    invoke the hashfunction(target_file) function on it, and return a set of hashed files

    Parameters:
    folder_name - The name of the folder you want to use (type string) enter a folder name in the immidiate directory
        or entry the direct path of the foldername
        
    output_in_terminal - If you want to print the resutls to the terminal (Type Boolean)

    return:
    returns the set of digests
    """

    # Define an empty set which will be used to store digest of files from folder Group1_Control_Hashed 
    hashed_files = set()

    # counter variable to keep track of the total files we have iterated over
    counter = 0

    # start of the loop
    for file in os.listdir(folder_name):
        file = os.path.join(folder_name, file)

        # create a temporary variable named temp_digest and set it equal to the result of hashfunction(file)
        # where folder_name is the current file in our loop
        temp_digest = hashfunction(file)

        # Add the digest to our set
        hashed_files.add(temp_digest)

        # increment counter by 1 at the end of loop
        counter = counter + 1


    # print out the set hashed_files, the counter variable, and the length of hashed_files
    if output_in_terminal:
        print(hashed_files)
        print(f"Our loop iterated a total of {counter} times")
        print(f"Our set of hash digests has a length of {len(hashed_files)}")

    return hashed_files


