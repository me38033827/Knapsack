

def knapsack_bottom_up_dp(w,v,W):

    plan=[]
    n=len(w)
    if W<min(w):
        return 0,[]

    if W>=sum(w):
        return sum(v),[i for i in range(1,n+1)]

    OPT=[([0] * (W+1)) for i in range(n+1)]

    for i in range(1,n+1):

        for j in range(1,W+1):

            if w[i-1]>j:
                OPT[i][j]=OPT[i-1][j]
            else:
                OPT[i][j]=max(OPT[i-1][j],OPT[i-1][j-w[i-1]]+v[i-1])

    i=n
    j=W
    while i>=1:
        if j-w[i-1]>=0 and j-w[i-1]<=W and OPT[i][j]==OPT[i-1][j-w[i-1]]+v[i-1]:
            plan.append(i)
            j-=w[i-1]
        i-=1



    return OPT[n][W],plan



w=[3,1,2]
v=[4,5,3]
W=100

OPT,plan=knapsack_bottom_up_dp(w,v,W)

print OPT
print plan


