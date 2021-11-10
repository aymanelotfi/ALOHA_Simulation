nbr_slots=4
nbr_users=4
#Things to add : calc pi , qi
# the graph with adjancency_matrix
def metricG(nbr_users,nbr_slots):
    return nbr_users/nbr_slots
def calc_lambda(G_users):
    ans=0
    d=[0]*(nbr_slots+1)
    for user in range(1,nbr_users+1):
        d[len(G_users[user])]+=1
    for degree in range(2,nbr_slots+1):
        ans+=d[degree]*degree
    lambda_=[0]*(nbr_slots+1)
    assert ans!=0,"Empty Graph !"
    for l in range(2,nbr_slots+1):
        lambda_[l]=(l*d[l])/ans
    return lambda_
def calc_mu(G_slots):
    ans=0
    d=[0]*(nbr_users+1)
    for slot in range(1,nbr_slots+1):
        d[len(G_slots[slot])]+=1
    for degree in range(2,nbr_users+1):
        ans+=d[degree]*degree
    mu=[0]*(nbr_users+1)
    assert ans!=0,"Empty Graph !"
    for l in range(2,nbr_users+1):
        mu[l]=(l*d[l])/ans
    return mu

G_users=[[] for _ in range(0,nbr_users+1)]
G_slots=[[] for u in range(0,nbr_slots+1)]
G_users[1]=[1,4]
G_users[2]=[1,4]
G_users[3]=[1,2,3]
G_users[4]=[3,4]
G_slots[1]=[1,2,3]
G_slots[2]=[3]
G_slots[3]=[3,4]
G_slots[4]=[1,2,4]
print(calc_lambda(G_users))
#print(calc_mu(G_slots))

while True:
    any_one=False
    known=-1
    for i in range(1,nbr_slots+1):
        if len(G_slots[i])==1:
            # check if any slot have degree 1
            known=G_slots[i][0]
    if known !=-1 :
        # free all edges from known
        for u in G_users[known]:
            G_slots[u].remove(known)
        G_users[known]=[]
    else:
        break
for u in range(1,nbr_users+1):
    if len(G_users[i]):
        print("Bad Protocol !")
        break
