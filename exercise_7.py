
def histo(a):
    for i in range(len(a)):
        if isinstance(a[i],int):
            t=""
            k=0
            while k < int(a[i]):
                t=t+"#"
                k=k+1
            a[i]=t
        else:
            a[i]="None"
l=[12, 2 ,6,'a']
histo(l)
print('\n' .join([str(myelement) for myelement in l]))
