import pandas as pd




def convert_list_of_dics_to_df(df , col_name):
	'''
	This function conerts a list of dics ['qualifications'/'specialities'] column to a dataframe
	which can be easily feeded to our dedupe model
	'''
	doctor_id = df.loc[:, "doctor_id"]
	col_name = df.loc[:, col_name]
	dfs  = []
    
	for doctor_id , data in zip(doctor_id , col_name):
		a = pd.DataFrame(eval(data))
		a.insert(0, 'doctor_id', doctor_id)
		dfs.append(a)
	merged = pd.concat(dfs)
	return merged



def merge_same_doctors_data(df , new_df):

    new_df = new_df.astype(str)

    dfs = []
    for col in new_df.columns:
        lis = []
        if col != 'doctor_id':
            for d in new_df.groupby('doctor_id')[col].apply(' -#- '.join):
                lis.append(d)
            t = pd.DataFrame(lis)[0].str.split('-#-' , expand = True)
            dic = {}
            for i in range(t.shape[1]):
                dic[i] = col + '_' + str(i + 1)
            t = t.rename(dic , axis = 'columns')
            dfs.append(t)
    wow = pd.concat(dfs , axis = 'columns')
    wow.insert(0 , 'doctor_id' , df['doctor_id'])
    df = pd.merge(df, wow, on='doctor_id')
    return df


def Preprocessing(path):
    x_df = pd.read_csv(path)
    x_df = x_df.drop_duplicates(keep="first")

    new_df = convert_list_of_dics_to_df(x_df , 'qualifications')
    x_df = merge_same_doctors_data(x_df , new_df)
    new_df = convert_list_of_dics_to_df(x_df , 'specialties')
    x_df = merge_same_doctors_data(x_df , new_df)


    x_df.drop(['qualifications' , 'specialties'], axis = 1 , inplace = True)
    x_df.dropna(thresh=0.1 * len(x_df),axis = 'columns',inplace=True)

    return x_df

def set_doctor_id_as_index(df):
    df.set_index('doctor_id' , inplace = True)
    return df



path = '../Dataset/Doctors_Data.csv'
df = Preprocessing(path)
df.to_csv('../Dataset/Doctors_Data_Preprocessed.csv')
df.tail(10).to_csv('../Dataset/mock_data.csv')