import jellyfish
import csv
import re
from unidecode import unidecode

def leveenshtien_calculator(str1, str2, weightage):
    score = jellyfish.levenshtein_distance(str1, str2)
    return score <= weightage

def jaro_calculator(str1,str2):
    if jellyfish.jaro_winkler_similarity(str1, str2) >= 0.7:
        return True

def damerau_calculator(str1,str2):
    if jellyfish.damerau_levenshtein_distance(str1, str2) == 1:
        return True

def match_calculator(str1,str2):
    if jellyfish.match_rating_comparison(str1, str2):
        return True


def preProcess(column):
    column = unidecode(column)
    column = re.sub('  ', ' ', column)
    
    if not column:
        column = None
    return column


def readData(file_name):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        data = {}
        for row in reader:
            clean_row = [(k, preProcess(v)) for (k, v) in row.items()]
            row_id = int(row['id'])
            data[row_id] = dict(clean_row)
    return data


def is_duplicate(database, r_data, param):
    for i in range(0, len(r_data)):
        for j in range(i + 1, len(database) + 1):
            if "leven" in  param:
                is_check = leveenshtien_calculator(r_data[i], database[j]['name'], 4)
                if is_check:
                    print(r_data[i], database[j]['name'])
            if "jaro" in  param:
                is_check = jaro_calculator(r_data[i], database[j]['name'])
                if is_check:
                    print(r_data[i], database[j]['name'])
            if "damerau" in  param:
                is_check = damerau_calculator(r_data[i], database[j]['name'])
                if is_check:
                    print(r_data[i], database[j]['name'])
            if "match" in  param:
                is_check = match_calculator(r_data[i], database[j]['name'])
                if is_check:
                    print(r_data[i], database[j]['name'])


data = readData("find_duplicates.csv")
is_duplicate(data, ['abhay dhiman'], 'leven')
