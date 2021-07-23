import pandas as pd
from trie_implementation import Trie

trie = Trie()


def create_trie_obj(col_name):
	col = pd.read_csv("../Dataset/Doctors_Data_Preprocessed.csv")[col_name]
	for val in col:
		trie.insert(str(val))
	return trie

# Creating a trie for doctor_id which we can store in our database , so query time will be constant
doctor_id_trie = create_trie_obj('doctor_id')

file = open("trie_cache.txt","a")
file.write(str(doctor_id_trie.root)) # saving as cache
# file = open("MyFile.txt","r+")
# print(file.read())
file.close()