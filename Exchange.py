seq1 = input()
seq2 = input()
transition = 0
transversion=0

for i in range(len(seq1)):
    if (seq1[i]=='A')&(seq2[i]=='G'): transition+=1
    if (seq1[i]=='G')&(seq2[i]=='A'): transition+=1
    if (seq1[i]=='C')&(seq2[i]=='T'): transition+=1
    if (seq1[i]=='T')&(seq2[i]=='C'): transition+=1

    if (seq1[i]=='A')&(seq2[i]=='T')|(seq1[i]=='A')&(seq2[i]=='C')|(seq1[i]=='G')&(seq2[i]=='T')|(seq1[i]=='G')&(seq2[i]=='C')\
        |(seq1[i]=='T')&(seq2[i]=='A')|(seq1[i]=='T')&(seq2[i]=='G')|(seq1[i]=='C')&(seq2[i]=='A')|(seq1[i]=='C')&(seq2[i]=='G'): transversion+=1
   
print(transition/transversion)


