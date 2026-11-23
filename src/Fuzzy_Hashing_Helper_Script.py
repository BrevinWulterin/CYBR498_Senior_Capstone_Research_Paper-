"""

Class:      CYBR 498

Student:    Brevin Wulterin

This script will use the PPDEEP library to create a fuzzy hash digest of all
100 files in a folder (which will be passed in as a string to our function
fuzzy_hash_function(folder_name, output_in_terminal). The digest (key) of each
fuzzy hash digest will be added to a dictionary along with the filename (value)


"""



import os
import ppdeep




def fuzzy_hash_function(folder_name, output_in_terminal):
    """
    Purpose: This function will iterate throuh each individual file in a folder
             invoke the fuzzy hash function on it, and adds those values to a dictionary

    Parameters: folder_name = name of the folder to be hashed (will only work on folders
                    with .py files)
                output_in_terminal = if True, will print out the digests, how many times
                    the for loop iterated, and the total length of the dictionary (mainly for troubleshooting purposes)
    return: fuzzy_hash_digests = a variable type dictionary. Key is a string(name of file)
                and the value is a string(fuzzy digest)
                
                    
    """

    # here is a dictionary which will create 
    fuzzy_hash_digests = {}


    # this counter variable will keep track of the total number of files we have iterated over
    counter = 0

    # start of the loop
    for file in os.listdir(folder_name):
        filepath = os.path.join(folder_name, file)

        # create a temp digest variable
        temp_fuzzy_digest = ppdeep.hash_from_file(filepath)

        # now we can add it to the dictionary (key is filepath, value is fuzzy digest}
        fuzzy_hash_digests[filepath] = temp_fuzzy_digest

        # keeping track of how many iterations we have made
        counter = counter+1

    # like in the Standard_Hash_Script we will output statistics to the termincal
    # if the we pass in a True value as an argument for the parameter of output_in_terminal
    if output_in_terminal:
        print(fuzzy_hash_digests)
        print(f"Our loop iterated a total of {counter} times")
        print(f"Our dictionary has a length of {len(fuzzy_hash_digests)}")
        
    return fuzzy_hash_digests

    
fuzzy_hash_function("Group1_Control_Hashed",False)
