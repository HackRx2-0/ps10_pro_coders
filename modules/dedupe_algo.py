import jellyfish
import csv
import re
import pandas as pd
from unidecode import unidecode
from .preprocessing import Preprocessing
import time
from .clusters import get_clusters, match_score


def leveenshtien_calculator(str1, str2, weightage):
    score = jellyfish.levenshtein_distance(str1, str2)
    return score <= weightage

def jaro_calculator(str1, str2, weightage):
    score = jellyfish.jaro_winkler_similarity(str1, str2)
    return score >= weightage

def damerau_calculator(str1,str2, weightage):
    score = jellyfish.damerau_levenshtein_distance(str1, str2)
    return score >= weightage

def match_calculator(str1,str2, weightage):
    score = jellyfish.match_rating_comparison(str1, str2)
    return score >= weightage


def preProcess(column):
    try:
        column = int(column)
        return "INT"
    except:
        try:
            column = column.lower()
            return (re.sub('  ', ' ', column))
        except:
            pass


def readData(dataframe, column):
    df_col = dataframe[column]
    clean_col = preProcess(df_col)
    data = {column: clean_col}
    return data


def is_duplicate(database, incoming_df, column_name, param, weightage):
    new_entry_doctor_id = []
    database_doctor_id = []
    for i in range(0, len(incoming_df[column_name])):
        for j in range(0, len(database[column_name])):
            if "leven" in param:
                is_check = False
                mypre = preProcess(incoming_df[column_name][i])
                mypre2 = preProcess(database[column_name][j])
                if mypre != "INT" and mypre2 != "INT":
                    is_check = leveenshtien_calculator(mypre,mypre2, weightage)
                else:
                    if incoming_df[column_name][i] == database[column_name][j]:
                        is_check = True
                if is_check:
                    new_entry_doctor_id.append(incoming_df['doctor_id'][i])
                    database_doctor_id.append(database['doctor_id'][j])
                    # print("New Entry:- ", incoming_df['doctor_id'][i], ", Database Entry:- ", database['doctor_id'][j])
                    # print("New Entry:- ", incoming_df[column_name][i], ", Database Entry:- ", database[column_name][j])
                    # print("New Entry:- ", incoming_df['locality'][i], ", Database Entry:- ", database['locality'][j])
                    # print("New Entry:- ", incoming_df['locality_latitude'][i], ", Database Entry:- ", database['locality_latitude'][j])
                    # print("New Entry:- ", incoming_df['locality_longitude'][i], ", Database Entry:- ", database['locality_longitude'][j])

            if "jaro" in param:
                mypre = preProcess(incoming_df[column_name][i])
                mypre2 = preProcess(database[column_name][j])
                if mypre != "INT" and mypre2 != "INT":
                    is_check = jaro_calculator(mypre,mypre2, weightage)
                else:
                    if incoming_df[column_name][i] == database[column_name][j]:
                        is_check = True
                if is_check:
                    new_entry_doctor_id.append(incoming_df['doctor_id'][i])
                    database_doctor_id.append(database['doctor_id'][j])
            if "damerau" in  param:
                mypre = preProcess(incoming_df[column_name][i])
                mypre2 = preProcess(database[column_name][j])
                if mypre != "INT" and mypre2 != "INT":
                    is_check = damerau_calculator(mypre,mypre2, weightage)
                else:
                    if incoming_df[column_name][i] == database[column_name][j]:
                        is_check = True
                if is_check:
                    new_entry_doctor_id.append(incoming_df['doctor_id'][i])
                    database_doctor_id.append(database['doctor_id'][j])
            if "match" in  param:
                mypre = preProcess(incoming_df[column_name][i])
                mypre2 = preProcess(database[column_name][j])
                if mypre != "INT" and mypre2 != "INT":
                    is_check = match_calculator(mypre,mypre2, weightage)
                else:
                    if incoming_df[column_name][i] == database[column_name][j]:
                        is_check = True
                if is_check:
                    new_entry_doctor_id.append(incoming_df['doctor_id'][i])
                    database_doctor_id.append(database['doctor_id'][j])
    
    return (new_entry_doctor_id, database_doctor_id)

database = pd.read_csv(r'F:\ps10_pro_coders\Dataset\Doctors_Data_Preprocessed.csv')
print(database.tail(10))
print()

def deDupeAlgo(incoming_data, col_weights):
    # incoming_data = Preprocessing(incoming_data)
    print(incoming_data)
    duplicate_data = {}
    
    for columns, weights in col_weights.items():
        new_entry_doctor_id, database_doctor_id = is_duplicate(database, incoming_data, columns, 'leven', 1)
        
        if len(new_entry_doctor_id) != 0:
            duplicate_data['DataBaseEntry'] = database_doctor_id
            duplicate_data['NewEntry'] = new_entry_doctor_id
    
    length = len(duplicate_data["DataBaseEntry"])
    print("-"*50)
    d1,d2 = [],[]
    for i in range(length):
        ids_database = duplicate_data["DataBaseEntry"][i]
        ids_newentry = duplicate_data["NewEntry"][i]
        d1.append(get_clusters(ids_database, database))
        d2.append(get_clusters(ids_newentry, incoming_data))
    # for i in range(length):
    #     ids_database = duplicate_data["DataBaseEntry"][i]
    #     ids_newentry = duplicate_data["NewEntry"][i]
    #     # Get match score
    #     m_score = match_score(get_clusters(ids_database, database), get_clusters(ids_newentry, incoming_data))
    #     duplicate_data["DataBaseEntry"][i] = (duplicate_data["DataBaseEntry"][i], m_score)
    #     duplicate_data["NewEntry"][i] = (duplicate_data["NewEntry"][i], m_score)
    #     # break
    d1 = pd.concat(d1)
    d2 = pd.concat(d2)
    d1 = d1.drop_duplicates(subset='doctor_name', keep="first")
    d2 = d2.drop_duplicates(subset='doctor_name', keep="first")
    print(d1.head())
    return d1,d2
    # if list(col_weights.keys())[0] != 'doctor_name':
    #     return d1[['doctor_name',list(col_weights.keys())[0]]], d2[['doctor_name',list(col_weights.keys())[0]]]
    # else:
    #     return d1['doctor_name'], d2['doctor_name']


# deDupeAlgo(incoming_data, {"doctor_name": 4})
# s_time = time.time()
# df = pd.read_csv(r"E:\bajaj\New folder\ps10_pro_coders\Dataset\mock_data.csv")
# print(deDupeAlgo(df, {"doctor_name": 4}))                                         #Format == "data name" => [(doctor_id, match_score), ...]
# print(time.time() - s_time)
