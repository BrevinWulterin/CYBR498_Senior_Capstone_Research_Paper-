"""

Class:      CYBR 498

Student:    Brevin Wulterin

This script will compute the hash digest for each file in their respective folders.
It will then copmare the hash digests between different groups to see if there
are any identical matches. 



Important to know:
folder_2_files is a folder containing the 100 files from the Group1_Control_Hashed
folder, but folder_2_files are slightly modified. And folder folder_3_files are
completely different files.


"""
import os
import hashlib

# user defined import
import Standard_Hash_Helper_Script as SHHS


# use the folder_iteration(folder_name, output_in_terminal)from Standard_Hash_Script.py reffered to as SHHS
# to hash the files from Group2_ SlightlyModified_NotHashed folder
folder_1_files = SHHS.folder_iteration("Group1_Control_Hashed", False)
folder_2_files = SHHS.folder_iteration("Group2_SlightlyModified_NotHashed", False)
folder_3_files = SHHS.folder_iteration("Group3_NonRelated_NotHashedFiles", False)
folder_4_files = SHHS.folder_iteration("Group4_Identical_to_group1", False)


# Our counter variables
#will increment by one if there is a digest match between GROUP1_CONTROL_HASHED_FILE_HASHES and Group2_SlightlyModified_NotHashed
exact_digest_match_coutner = 0
exact_digest_match_coutner2 = 0
exact_digest_match_counter3 = 0
#will increment by one if there is no digest match between GROUP1_CONTROL_HASHED_FILE_HASHES and Group2_SlightlyModified_NotHashed
no_digest_match_coutner = 0
no_digest_match_coutner2 = 0
no_digest_match_counter3 = 0

for digest in folder_1_files:
    if digest in folder_2_files:
        exact_digest_match_coutner = exact_digest_match_coutner + 1
        #print(digest)
    else:
        no_digest_match_coutner = no_digest_match_coutner +1


for digest in folder_1_files:
    if digest in folder_3_files:
        exact_digest_match_coutner2 = exact_digest_match_coutner2 + 1
        #print(digest)
    else:
        no_digest_match_coutner2 = no_digest_match_coutner2 +1
        
for digest in folder_1_files:
    if digest in folder_4_files:
        exact_digest_match_counter3 = exact_digest_match_counter3 + 1
        #print(digest)
    else:
        no_digest_match_counter3 = no_digest_match_counter3 +1
        

print(f"There were a total of {exact_digest_match_coutner} matches between group 1 and 2")
print(f"There were a total of {exact_digest_match_coutner2} matches between group 1 and 3")
print(f"There were a total of {exact_digest_match_counter3} matches between group 1 and 4")
print(f"Which means there were a total of {no_digest_match_coutner} non matches between group 1 and 2")
print(f"Which means there were a total of {no_digest_match_coutner2} non matches between group 1 and 3")
print(f"Which means there were a total of {no_digest_match_counter3} non matches between group 1 and 4")

        





