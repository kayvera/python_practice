def recursiveDNA(nucleotides, newArr=None):
    if newArr is None:
        newArr = []
    newArr.append(nucleotides[:2])
    if len(nucleotides) > 2:
        recursiveDNA(nucleotides[2:], newArr)
    return newArr


arrDNA = ['A', 'T', 'C', 'G', 'T', 'A', 'G', 'C']

print(recursiveDNA(arrDNA))
