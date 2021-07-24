from dedupe_algo import readData, is_duplicate
# from preprocessing import Preprocessing
import logging
import time
import pandas as pd

logging.basicConfig(filename="dedupe.log", filemode="a",
                    format='%(asctime)s  %(levelname)s - %(message)s', datefmt='%Y-%m-%d  %H:%M:%S')

#Let us Create an object
logger = logging.getLogger()
#Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Importing the data
# df = Preprocessing(path="../Dataset/Doctors_Data.csv")
# data = readData(df, 'doctor_name')
data = pd.read_csv("F:\ps10_pro_coders\Dataset\Doctors_Data_Preprocessed.csv")
param_ls = ["leven", "damerau", "jaro", "match"]
data2 = pd.read_csv('F:\ps10_pro_coders\Dataset\mock_data.csv')

def edit_log(string):
    logger.info(string)

def calTimeLeven():
    start_time = time.time()
    is_duplicate(data, data2, 'doctor_name','leven', 4)
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by leveenshtien:- " + time_taken)

def calTimeDamerau():
    start_time = time.time()
    is_duplicate(data, data2, 'doctor_name', 'damerau', 4)
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by damerau:- " + time_taken)

def calTimejaro():
    start_time = time.time()
    is_duplicate(data, data2, 'doctor_name', 'jaro', 4)
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by jaro:- " + time_taken)


def calTimematch():
    start_time = time.time()
    is_duplicate(data, data2, 'doctor_name', 'match', 4)
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by match:- " + time_taken)


calTimeLeven()
calTimeDamerau()
calTimejaro()
calTimematch()
