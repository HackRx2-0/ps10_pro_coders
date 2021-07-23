import jellyfish
import csv
import re
from unidecode import unidecode
from preprocessing import Preprocessing

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


def preProcess(column_ls):
    data = []
    for i in range(len(column_ls)):
        column = column_ls[i]
        column = column.lower()
        data.append(re.sub('  ', ' ', column))
    return data

def readData(dataframe, column):
    df_col = dataframe[column]
    clean_col = preProcess(df_col)
    data = {column: clean_col}
    return data


def is_duplicate(database, r_data, param, weightage):
    for i in range(0, len(r_data)):
        for columns in database:
            if "leven" in param:
                is_check = leveenshtien_calculator(r_data[i].lower(), columns, weightage)
                if is_check:
                    print("New Entry:- ", r_data[i].lower(), ", Database Entry:- ", columns)
            if "jaro" in  param:
                is_check = jaro_calculator(r_data[i], columns, weightage)
                if is_check:
                    print(r_data[i], columns)
            if "damerau" in  param:
                is_check = damerau_calculator(r_data[i], columns, weightage)
                if is_check:
                    print(r_data[i], columns)
            if "match" in  param:
                is_check = match_calculator(r_data[i], columns, weightage)
                if is_check:
                    print(r_data[i], columns)

def deDupeAlgo(df):
    data = readData(df, 'doctor_name')
    is_duplicate(data['doctor_name'], ['Arunesh Dutt Upadhyay'], 'leven', 4)

df = Preprocessing(path = "../Dataset/Doctors_Data.csv")
deDupeAlgo(df)
