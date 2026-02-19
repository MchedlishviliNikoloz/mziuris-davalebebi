matrix = ( (1,2,3),
           (4,5,6),
           (7,8,9) )
for i in range(3):
    new_tup = ()
    for j in range(2,-1,-1):
        new_tup += (matrix[j][i],)
    print(new_tup)