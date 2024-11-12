Dna = input('Enter the strand of DNA')
revDna = Dna[::-1]
revComp = ''
for nt in revDna:
    if nt == 'A':
        revComp+='T'
    elif nt =='G':
        revComp+='C'
    elif nt =='C':
        revComp+='G'
    elif nt =='T':
        revComp+='A'
print(revComp)
