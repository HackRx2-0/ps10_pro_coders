from streamlit import *
import pandas as pd
import numpy as np

def get_features():
    data = pd.read_csv('Dataset/Doctors_Data_Preprocessed.csv')
    return data

set_option('deprecation.showfileUploaderEncoding', False)

title('De-Dupe Engine')

data = file_uploader("", type=["csv"])  # Loading the dataset
df = None
if data is not None:  # Here if block runs only when user gives dataset

    # Loading the dataset using pandas
    df = pd.read_csv(data)

text("OR")

real_Df = text_input("Enter Real Time data : ")

org_data = get_features()  # Getting the features from the dataset
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

if df is not None:
    button("find Duplicates on bases of incoming data",on_click="")

button("Find Duplicate in Database")
