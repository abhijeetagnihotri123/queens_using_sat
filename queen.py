import pycosat
res=[]
cnf=[]
def v(i,j):
    return 8*(i-1)+j
if __name__=="__main__":
    for i in range(1,9):
        res.append([v(i,j) for j in range(1,9)])
    for i in range(1,9):
        res.append([v(j,i) for j in range(1,9)])
    for i in range(1,9):
        for j in range(1,9):
            for k in range(j+1,9):
                res.append([-v(i,j),-v(i,k)])
    for i in range(1,9):
        for j in range(1,9):
            for k in range(j+1,9):
                res.append([-v(j,i),-v(k,i)])
    for i in range(1,9):
        for j in range(1,9):
            for i1 in range(i+1,9):
                for j1 in range(j+1,9):
                    if (i-j)==(i1-j1):
                        res.append([-v(i,j),-v(i1,j1)])
    for i in range(1,9):
        for j in range(1,9):
            for i1 in range(1,9):
                for j1 in range(1,9):
                    if (i!=i1) and (j!=j1) and (i+j)==(i1+j1):
                        res.append([-v(i,j),-v(i1,j1)])
    cnf=pycosat.solve(res)
    l=[]
    for i in range(1,9):
        l.append([0,0,0,0,0,0,0,0])
    for i in range(1,9):
        for j in range(1,9):
            if v(i,j) in cnf:
                l[i-1][j-1]=1
    for i in l:
        print(i)
    print("writing all the clauses generated in the file cl.cnf")
    file = open("cl.cnf","w")
    var1 = str(64)
    var2 = str(len(res))
    s = "p cnf "
    s = s + var1 +" "+ var2
    s = s + "\n"
    file.write(s)
    for i in res:
        l = i
        s=""
        l.append(0)
        for j in l:
            s+=str(j)+" "
        s = s + "\n"
        file.write(s)
    file.close()
