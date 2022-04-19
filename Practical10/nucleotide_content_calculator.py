def percentage(sq):
    """
    change letters in the sequence to upper case
    count number of A T C G respectibely
    return the percentage of A T C G
    """
    sq=sq.upper()
    a=sq.count('A')
    t=sq.count('T')
    c=sq.count('C')
    g=sq.count('G')
    pa=round(a/len(sq),2)
    pt=round(t/len(sq),2)
    pc=round(c/len(sq),2)
    pg=round(g/len(sq),2)
    op="percentage of A:"+str(pa)+"\n"+"percentage of T:"+str(pt)+"\n"+"percentage of C:"+str(pc)+"\n"+"percentage of G:"+str(pg)+"\n"
    print(op)   
    return op
s=input("input your DNA sequence:\n")
percentage(s)
    
