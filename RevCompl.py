from sys import stdin

seq = input()

compseq = []

for x in seq:
    if x == 'A': compseq.insert(0, 'T')
    if x == 'T': compseq.insert(0, 'A')
    if x == 'G': compseq.insert(0, 'C')
    if x == 'C': compseq.insert(0, 'G')
    else: pass

strcompseq = ''.join(compseq)
print(strcompseq)