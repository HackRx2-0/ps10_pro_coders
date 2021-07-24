from streamlit import *
import pandas as pd
import numpy as np
from modules.dedupe_algo import deDupeAlgo

def get_features():
    data = pd.read_csv('Dataset/Doctors_Data_Preprocessed.csv')
    return data

set_option('deprecation.showfileUploaderEncoding', False)

title('De-Dupe Engine')

data2 = file_uploader("", type=["csv"])  # Loading the dataset
df = None
if data2 is not None:  # Here if block runs only when user gives dataset

    # Loading the dataset using pandas
    df = pd.read_csv(data2)

# text("OR")

# real_Df = text_input("Enter Real Time data : ")

org_data = get_features()  # Getting the features from the dataset
del org_data['Unnamed: 0']
lis = org_data.columns

title("Dataset")
dataframe(org_data.head(3))

title("Let's Configure Weights!")
dic = {}
k = 0
for i in range(8):
    cols = beta_columns(4)
    for j in range(4):
        dic[lis[k]] = cols[j].number_input(f"{lis[k]}",value=0.5,key=f"{lis[k]}",min_value=0.0,max_value=1.0,step=0.0001)
        text("")
        k += 1
    text("")
ndic = {}
ndic['doctor_name'] = dic['doctor_name']
ndic['locality'] = dic['locality']
ndic['clinic_name'] = dic['clinic_name']
duplicate_data = None

d1,d2 = None,None
if df is not None:
    if button("find Duplicates on bases of incoming data"):
        d1,d2 = deDupeAlgo(df,ndic)

if d1 is not None:
    col1,col2 = beta_columns(2)
    del d1['Unnamed: 0']
    col1.dataframe(d1)
    col2.dataframe(d2)

# button("Find Duplicate in Database")
