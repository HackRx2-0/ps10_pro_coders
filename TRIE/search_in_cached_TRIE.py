from trie_implementation import Trie

file = open("trie_cache.txt","r+")
cached_trie = dict(eval(file.read()))
doctor_id_trie = Trie(cached_trie)

# print(doctor_id_trie.search('477320'))

import pandas as pd
df = pd.read_csv('../Dataset/Doctors_Data_Preprocessed.csv')

print(doctor_id_trie.search("271984"))
# sum_val = 0
# for val in df.doctor_id:
# 	sum_val += doctor_id_trie.search(271984)

# print(sum_val , len(df.doctor_id))