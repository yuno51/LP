import numpy as np
from fractions import Fraction

f = np.frompyfunc(lambda x: Fraction(x,1), 1, 1)


new_float = np.frompyfunc(float, 1,1)


def change_var(dic, r, c):
    #r:列, c:行
    LP_dict = dic[:, :]

    new_row = (- LP_dict[:, r] / LP_dict[c,r]).reshape(-1,1)
    new_row[c,0] = 0
    LP_dict = LP_dict + new_row * LP_dict[c, :]
    new_row[c,0] = -1 /LP_dict[c,r]
    LP_dict[c,:] = -LP_dict[c,:] / LP_dict[c,r]
    LP_dict[:,r] = -new_row.flatten()
    print(new_float(LP_dict))
    return LP_dict

    




def simplex(var_min, var_max, c:np.array, A:np.array, b:np.array, _2flag=False):
    #c = np.array([0, 5, -5, 1])
    #A = np.array([[1,4,2], [-2,1,4], [8,-3,-6]])
    #b = np.array([7,1,5])

    if len(b[b<0])> 0 and _2flag:
        print("二段階")
        auxA = np.c_[A, f(np.where(b < 0, -1, 0))]
        simplex(0, 1000, f([0,0,0,0,-1]), auxA, b, False)


    LP_dict =np.r_[c.reshape(1,-1), np.c_[b.reshape(-1,1), -A]]
    print(new_float(LP_dict))
    while True:
        try:
            LP_dict = change_var(LP_dict, int(input()),int(input()))
        except:
            break
    return LP_dict






'''
#1-1
A = [[1,4,2], [-2,1,4], [8,-3,-6]]
A = f(A)
b = [7,1,5]
b = f(b)
c = [0, 5,-5,1]
c = f(c)
simplex(0,1000 ,c, A, b)
'''


#A,bはそのまま書く、cは定数(多くは0)も入れて書く
#列、行の順で指定


A = f([[3,1,0], [5,2,-1], [7,3,-1]])
b = f([3,4,8])
c = f([0,1,-4,1])
print(simplex(0,1000 ,c, A, b, False))
