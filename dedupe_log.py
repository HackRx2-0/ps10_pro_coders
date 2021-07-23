from k_algo import is_duplicate, readData
import logging
import time

logging.basicConfig(filename="dedupe.log", filemode="a",
                    format='%(asctime)s  %(levelname)s - %(message)s', datefmt='%Y-%m-%d  %H:%M:%S')

#Let us Create an object
logger = logging.getLogger()
#Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Importing the data
data = readData("find_duplicates.csv")
param_ls = ["leven", "damerau", "jaro", "match"]


def edit_log(string):
    logger.info(string)

def calTimeLeven():
    start_time = time.time()
    is_duplicate(data, "leven")
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by leveenshtien:- " + time_taken)

def calTimeDamerau():
    start_time = time.time()
    is_duplicate(data, "damerau")
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by damerau:- " + time_taken)

def calTimejaro():
    start_time = time.time()
    is_duplicate(data, "jaro")
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by jaro:- " + time_taken)


def calTimematch():
    start_time = time.time()
    is_duplicate(data, "match")
    end_time = time.time()
    time_taken = str(round(end_time - start_time, 4))
    edit_log("Time Taken by match:- " + time_taken)


calTimeLeven()
calTimeDamerau()
calTimejaro()
calTimematch()