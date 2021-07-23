from streamlit import *
import pandas as pd
import numpy as np
from Preprocessing_Data.preprocessing import Preprocessing


def get_features():
    data = Preprocessing("Dataset/Doctors_Data.csv")
    return data.columns

set_option('deprecation.showfileUploaderEncoding', False)

title('De-Dupe Engine')

data = file_uploader("", type=["csv"])  # Loading the dataset
df = None
if data is not None:  # Here if block runs only when user gives dataset

    # Loading the dataset using pandas
    df = pd.read_csv(data)

text("OR")

real_Df = text_input("Enter Real Time data : ")

lis = get_features()  # Getting the features from the dataset

title("Let's Configure Weights!")

k = 0
for i in range(8):
    cols = beta_columns(4)
    for j in range(4):
        cols[j].number_input(f"Configure {lis[k]}",value=0.5,key=f"{lis[k]}",min_value=0.0,max_value=1.0,step=0.0001)
        text("")
        k += 1

if df is not None:
    button("find Duplicates on bases of incoming data")

button("Find Duplicate in Database")
