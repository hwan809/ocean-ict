n,m=map(int,input().split())
lst1=list(map(int,input().split()))
lst2=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and k!=i and lst1[i] + lst1[j] + lst1[k]<=m:
                lst2.append(lst1[i] + lst1[j] + lst1[k])
                print(i, j, k)
                               
print(max(lst2)) 