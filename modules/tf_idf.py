import time
import pandas as pd
import sparse_dot_topn.sparse_dot_topn as ct
from scipy.sparse import csr_matrix
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re
# from ps10_pro_coders.modules.preprocessing import Preprocessing


def ngrams(string, n=3):
    string = re.sub(r'[,-./]|\sBD', r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


def awesome_cossim_top(A, B, ntop, lower_bound=0):
    # force A and B as a CSR matrix.
    # If they have already been CSR, there is no overhead
    A = A.tocsr()
    B = B.tocsr()
    M, _ = A.shape
    _, N = B.shape

    idx_dtype = np.int32

    nnz_max = M*ntop

    indptr = np.zeros(M+1, dtype=idx_dtype)
    indices = np.zeros(nnz_max, dtype=idx_dtype)
    data = np.zeros(nnz_max, dtype=A.dtype)

    ct.sparse_dot_topn(
        M, N, np.asarray(A.indptr, dtype=idx_dtype),
        np.asarray(A.indices, dtype=idx_dtype),
        A.data,
        np.asarray(B.indptr, dtype=idx_dtype),
        np.asarray(B.indices, dtype=idx_dtype),
        B.data,
        ntop,
        lower_bound,
        indptr, indices, data)

    return csr_matrix((data, indices,indptr),shape=(M,N))


def get_matches_df(sparse_matrix, name_vector, top=100):
    non_zeros = sparse_matrix.nonzero()

    sparserows = non_zeros[0]
    sparsecols = non_zeros[1]

    if top:
        nr_matches = top
    else:
        nr_matches = sparsecols.size

    left_side = np.empty([nr_matches], dtype=object)
    right_side = np.empty([nr_matches], dtype=object)
    similairity = np.zeros(nr_matches)

    for index in range(0, nr_matches):
        left_side[index] = name_vector[sparserows[index]]
        right_side[index] = name_vector[sparsecols[index]]
        similairity[index] = sparse_matrix.data[index]

    return pd.DataFrame({'left_side': left_side,
                         'right_side': right_side,
                         'similairity': similairity})


# df = Preprocessing(r"E:\bajaj\New folder\ps10_pro_coders\Dataset\Doctors_Data.csv")
# train_df = df.iloc[:7]
# test_df = pd.DataFrame({"doctor_name": ["Arunesh Dutt", "Renu Mahtani", "Manoj Madhukar Deshpande", "aaditya", "manav", "abhay", "ayush"]})
# print("Train Data:- ")
# print(train_df.head())
# print()
# print("Test Data:- ")
# print(test_df.head())
# print()

# train_df = pd.concat([train_df, test_df], ignore_index=True)

# train_doctor_names = train_df['doctor_name']
# vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams)
# train_tf_idf_matrix = vectorizer.fit_transform(train_doctor_names)


# t1 = time.time()
# matches = awesome_cossim_top(train_tf_idf_matrix, train_tf_idf_matrix.transpose(), 10, 0.8)
# t = time.time()-t1
# print("SELFTIMED:", t)

# matches_df = get_matches_df(matches, train_doctor_names, top=7)
# matches_df = matches_df[matches_df['similairity'] < 0.99999]  # Remove all exact matches
# print(matches_df.head())
