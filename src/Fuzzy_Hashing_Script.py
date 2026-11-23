"""
Class: CYBR 498

Student: Brevin Wulterin

This file will use the ppdeep library alongside the user defined script 
Fuzzy_Hash_Script to fuzzy hash each folder in the project. Then the file
will determine if there are similarities between folder_1, folder_2, and folder_3
while keeping track of false positive and true positive rates

"""


import os
import ppdeep

import Fuzzy_Hashing_Helper_Script as FHHS



# Use the fuzzy_hash_function(folder_name, output_in_terminal) to fuzzyhash files from folder 2 and three
GROUP1_Control_Hashed = FHHS.fuzzy_hash_function("Group1_Control_Hashed", False)
folder_2_file_hashes = FHHS.fuzzy_hash_function("Group2_SlightlyModified_NotHashed", False)
folder_3_file_hashes = FHHS.fuzzy_hash_function("Group3_NonRelated_NotHashedFiles", False)
folder_4_file_hashes = FHHS.fuzzy_hash_function("Group4_Identical_to_group1", False)



# Our counter variables
#will increment by one if there is a digest match between GROUP1_CONTROL_HASHED_FILE_HASHES, Group2_SlightlyModified_NotHashed, Group4_Identical_to_group1
true_positive_group2 = 0
false_positive_group3 = 0
true_positive_group4 = 0

#will increment by one if there is no digest match between GROUP1_CONTROL_HASHED_FILE_HASHES, Group2_SlightlyModified_NotHashed, Group4_Identical_to_group1
false_negative_group2 = 0
true_negative_gropu3 = 0
false_negative_group4 = 0

# due to fuzzy hashing, we have to define a similarity threshold between 0 and 100
SIMILARITY_THRESHOLD = 50

# iterate through each item in the dictionary

for file1_name, fuzzy_digest1 in GROUP1_Control_Hashed.items():

    # now we will iterate through group 2 and 3 in seperate for loops (and compare files by filesname, keeping track of match and no match counts
    for file2_name, fuzzydigest2 in folder_2_file_hashes.items():
        temp_result = ppdeep.compare(fuzzy_digest1,fuzzydigest2)

        if temp_result > SIMILARITY_THRESHOLD:
            true_positive_group2 = true_positive_group2 + 1
        else:
            false_negative_group2 = false_negative_group2 + 1

    for file3_name, fuzzydigest3 in folder_3_file_hashes.items():
        temp_result = ppdeep.compare(fuzzy_digest1, fuzzydigest3)

        if temp_result >= SIMILARITY_THRESHOLD:
            false_positive_group3 = false_positive_group3 + 1
        else:
            true_negative_gropu3 = true_negative_gropu3 + 1

    for file3_name, fuzzydigest4 in folder_4_file_hashes.items():
        temp_result = ppdeep.compare(fuzzy_digest1, fuzzydigest4)

        if temp_result >= SIMILARITY_THRESHOLD:
            true_positive_group4 = true_positive_group4 + 1
        else:
            false_negative_group4 = false_negative_group4 + 1

print(f"Group 2 matches (true positives) = {true_positive_group2}")

print(f"Group 3 false positives {false_positive_group3}")

print(f"Group 4 true_positives {true_positive_group4}")

        
        
    

