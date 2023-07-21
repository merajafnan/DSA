
def lcs_recurssive(seq1,seq2,idx1,idx2):
    
    if idx1 == 0 or idx2 == 0:
        return 0
    
    elif seq1[idx1-1] == seq2[idx2-1]:
        return 1 + lcs_recurssive(seq1,seq2,idx1-1,idx2-1)
    
    else:
        option1 = lcs_recurssive(seq1,seq2,idx1-1,idx2)
        option2 = lcs_recurssive(seq1,seq2,idx1,idx2-1)
        return max(option1,option2)
    
seq1 = 'srendipitous'
seq2 = 'precipitation'
result = lcs_recurssive(seq1,seq2,len(seq1),len(seq2))
print(result)