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