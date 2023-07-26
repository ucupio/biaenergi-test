def intersect(bagA, bagB):
    setB = set(bagB)
    return [x for x in bagA if x in setB]

print(intersect([1,2,3],[2,3,4]))