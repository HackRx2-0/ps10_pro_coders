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



def test(df , new_df):

    new_df = new_df.astype(str)

    dfs = []
    for col in new_df.columns:
        lis = []
        if col != 'doctor_id':
            for d in new_df.groupby('doctor_id')[col].apply(' -#- '.join):
                lis.append(d)
            t = pd.DataFrame(lis)[0].str.split('-#-' , expand = True).rename({0 : '0' + col , 1 : '1' + col , 2 : '2' + col} , axis = 'columns')
            dfs.append(t)
    wow = pd.concat(dfs , axis = 'columns')
    wow.insert(0 , 'doctor_id' , df['doctor_id'])
    df = pd.merge(df, wow, on='doctor_id')
    return df



x_df = pd.read_csv("../Dataset/Doctors_Data.csv")

new_df = convert_list_of_dics_to_df(x_df , 'qualifications')
x_df = test(x_df , new_df)
new_df = convert_list_of_dics_to_df(x_df , 'specialties')
x_df = test(x_df , new_df)


x_df.drop(['qualifications' , 'specialties'], axis = 1 , inplace = True)
print(x_df)