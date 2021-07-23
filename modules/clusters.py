import pandas as pd

def get_clusters(id, df):
    return df.loc[df['doctor_id'] == id]

def match_score(row_1, row_2):
    col_1 = row_1.values.tolist()[0]
    col_2 = row_2.values.tolist()[0]
    count_match = 0

    mis_matches = 0
    for column_1, column_2 in zip(col_1, col_2):
        if column_1 and column_2:
            if column_1 == column_2:
                count_match += 1
    
    try:
        return count_match / (len(col_1) - mis_matches)
    except:
        return 1

def average(lst):
    return sum(lst) / len(lst)

def avg_weight(w, avrg):
    for key in w.keys():
        for value in w[key]:
            if value >= avrg:
                print('Weight: ' + str(value) + ' greater than: ' + str(avrg))

if __name__ == '__main__':
    lst = [12, 34, 4, 2]
    avg = average(lst)
    print('Average is: ' + str(avg))
    dic = {'w1': [11, 45, 32], 'w2' : [4, 9, 12], 'w3' : [65, 8, 0]}
    avg_weight(dic, avg)
