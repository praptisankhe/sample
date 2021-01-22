import csv

with open("1.csv") as i:
    cfile=csv.reader(i)
    d=list(cfile)
    
    sh=d[1][:-1]
    gh=[['?' for i in range(len(sh))] for j in range(len(sh))]
    
    print("\nCANDIDATE ELIMINATION ALGORITHM")
    for i1 in d:
        if i1[-1]=="Yes":
            for j in range(len(sh)):
                if i1[j]!=sh[j]:
                    sh[j]='?'
                    gh[j][j]='?'
        
        elif i1[-1]=="No":
            for j in range(len(sh)):
                if i1[j]!=sh[j]:
                    gh[j][j]=sh[j]
                else:
                    gh[j][j]="?"
        print("\nStep:",d.index(i1)+1)
        print("Specific Hypothesis: ", sh)
        print("General Hypothesis: ",gh) 
    
    genh=[]

    for i in gh:
        for j in i:
            if j!='?':
                genh.append(i)
                break

    print("\nFinal specific hypothesis:\n",sh)

    print("\nFinal general hypothesis:\n",genh)