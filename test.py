import numpy as np
# from knapsack_bottom_up_dp import knapsack_bottom_up_dp as bu
# from knapsack_top_down_dp import knapsack_top_down_dp as td
from bruteforce import knapsack_bf as bf
import time
import sys
import pandas as pd

sys.setrecursionlimit(3000000)

bf_data=dict()
# td_data=dict()
# bu_data=dict()

capacity=list()
#
# # for i in range(1,23):
# #     bf_data['n='+str(i)]=list()
# #     td_data['n='+str(i)]=list()
# #     bu_data['n='+str(i)]=list()
#
for W in range (500,15500,500):
    capacity.append(W)


bf_data['runtime']=list()

for i in range(500,15500,500):
    # bf_data['n='+str(i)]=list()
    # td_data['n='+str(i)]=list()
    # bu_data['n='+str(i)]=list()
    print(i)

    w=np.random.randint(1000,100000, size=17)
    v=np.random.randint(5,100,size=17)

    bf_time=0


    for j in range(3):
        t1=time.time()
        bf(w,v,i)
        t2=time.time()
        bf_time+=(t2-t1)

    bf_time=bf_time/3.0


    bf_data['runtime'].append(bf_time)

bf_data['capacity']=capacity



bf_csv=pd.DataFrame(data=bf_data)




bf_csv.to_csv('data/bruteforce_fixed_n10.csv')






#
# a={}
#
# for i in range(1000,3000,1000):
#     a[i]={}
#
# for i in range(1000,3000,1000):
#     w=np.random.randint(10, size=i)
#     v=np.random.randint(30,size=i)
#
#
#     for j in range(1000,3000,1000):
#         t1=time.time()
#         bu(w,v,j)
#         t2=time.time()
#         a[i].update({j:t2-t1})
#         print('n=',i,'W=',j)
#         print(t2-t1,'s')
#
#
# print(a)

# w=np.random.randint(10,100, size=20000)
# v=np.random.randint(1,20,size=20000)


# print(bu(w,v,100))
# t1=time.time()
# print(bu(w,v,20000))
# t2=time.time()
# print('n=1000',t2-t1)
# # print(td(v,w,8))



# for i in range(3,20):
#     for j in range(1,30):
#         w=np.random.randint(1,10, size=i)
#         v=np.random.randint(1,20,size=i)
#         print(i)
#         print(j)
#         val1,plan1=bu(w,v,j)
#         val2,plan2=bf(w,v,j)
#         # val3,plan3=td(v,w,j)
#         if(val1!=val2):
#             print("i=",i,'j=',j)




# bf_data['capacity']=capacity
# td_data['capacity']=capacity
# bu_data['capacity']=capacity
#
#
# bf_csv=pd.DataFrame(data=bf_data)
# td_csv=pd.DataFrame(data=td_data)
# bu_csv=pd.DataFrame(data=bu_data)
#
#
#
#
# bf_csv.to_csv('data/bruteforce.csv')
# td_csv.to_csv('data/topdown.csv')
# bu_csv.to_csv('data/buttomup.csv')
