import numpy as np
import matplotlib.pyplot as plt
def generate_graph(lambda_,nbr_users,nbr_slots):
    degree=list(np.random.choice(len(lambda_),nbr_users,lambda_))
    degree=[0]+degree
    G_users=[[] for _ in range(nbr_users+1)]
    G_slots=[[] for _ in range(nbr_slots+1)]
    for u in range(1,nbr_users+1):
        l=list(np.random.choice(nbr_slots, degree[u], replace=False))
        G_users[u]=[slot+1 for slot in l]
        for d in G_users[u]:
            G_slots[d].append(u)
    return (G_users,G_slots)
def calc_G_T(Graph):
    G_users=Graph[0]
    G_slots=Graph[1]
    nbr_users=len(G_users)-1
    nbr_slots=len(G_slots)-1
    s=0
    while True:
        known=-1
        for i in range(1,nbr_slots+1):
            if len(G_slots[i])==1:
                # check if any slot have degree 1
                known=G_slots[i][0]

        if known !=-1 :
            # free all edges from known
            s+=1
            for u in G_users[known]:
                G_slots[u].remove(known)
            G_users[known]=[]
        else:
            break
    return (nbr_users/nbr_slots,s/nbr_slots)
G_=[]
T_=[]
lambda_=[0,1]
iter=500
nbr_users=10
nbr_slots=100
for i in range(iter):
    ans=[0,0]
    for j in range(10):
        data=calc_G_T(generate_graph([0,1],nbr_users,nbr_slots))
        ans[0]+=data[0]
        ans[1]+=data[1]
    ans[0]/=10
    ans[1]/=10
    G_.append(ans[0])
    T_.append(ans[1])
    nbr_users+=1
    #print(data)

plt.plot(G_,T_)
plt.show()
