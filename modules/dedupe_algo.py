import jellyfish
import csv
import re
import pandas as pd
from unidecode import unidecode
from preprocessing import Preprocessing
import time

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
                is_check = leveenshtien_calculator(preProcess(incoming_df[column_name][i]), preProcess(database[column_name][j]), weightage)
                if is_check:
                    new_entry_doctor_id.append(incoming_df['doctor_id'][i])
                    database_doctor_id.append(database['doctor_id'][j])
                    # print("New Entry:- ", incoming_df['doctor_id'][i], ", Database Entry:- ", database['doctor_id'][j])
                    # print("New Entry:- ", incoming_df[column_name][i], ", Database Entry:- ", database[column_name][j])
                    # print("New Entry:- ", incoming_df['locality'][i], ", Database Entry:- ", database['locality'][j])
                    # print("New Entry:- ", incoming_df['locality_latitude'][i], ", Database Entry:- ", database['locality_latitude'][j])
                    # print("New Entry:- ", incoming_df['locality_longitude'][i], ", Database Entry:- ", database['locality_longitude'][j])

            if "jaro" in param:
                is_check = jaro_calculator(incoming_df[i], database[j], weightage)
                if is_check:
                    print(incoming_df[i], database[j])
            if "damerau" in  param:
                is_check = damerau_calculator(incoming_df[i], database[j], weightage)
                if is_check:
                    print(incoming_df[i], database[j])
            if "match" in  param:
                is_check = match_calculator(incoming_df[i], database[j], weightage)
                if is_check:
                    print(incoming_df[i], database[j])
    
    return (new_entry_doctor_id, database_doctor_id)

database = pd.read_csv(r'E:\bajaj\New folder\ps10_pro_coders\Dataset\Doctors_Data_Preprocessed.csv')
print(database.tail(10))
print()

def deDupeAlgo(incoming_data, col_weights):
    # incoming_data = Preprocessing(df)
    print(incoming_data)
    duplicate_data = {}
    
    for columns, weights in col_weights.items():
        new_entry_doctor_id, database_doctor_id = is_duplicate(database, incoming_data, columns, 'leven', 3)
        
        if len(new_entry_doctor_id) != 0:
            duplicate_data['DataBaseEntry'] = database_doctor_id
            duplicate_data['NewEntry'] = new_entry_doctor_id
    
    return duplicate_data


# deDupeAlgo(incoming_data, {"doctor_name": 4})
s_time = time.time()
df = pd.read_csv(r"E:\bajaj\New folder\ps10_pro_coders\Dataset\mock_data.csv")
print(deDupeAlgo(df, {"doctor_name": 4}))
print(time.time() - s_time)
