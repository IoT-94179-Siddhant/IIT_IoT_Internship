#matrix 1:3x4 list of lists
matrix_list=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#matrix 2:3x4 tuple of tuples
matrix_tuple=(
    (12,11,10,9),
    (8,7,6,5),
    (4,3,2,1)
)

#function to calculate addition and subtraction
def add_sub_matrices(m1,m2):
    add_result=[]
    sub_result=[]

    for i in range(3):
        add_row=[]
        sub_row=[]
        for j in range(4):
            add_row.append(m1[i][j]+m2[i][j])
            sub_row.append(m1[i][j]-m2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)

    return add_result,sub_result

#main code
addition,subtraction=add_sub_matrices(matrix_list,matrix_tuple)
print("Addition Result:")
for row in addition:
    print(row)
print("\nSubtraction Result:")
for row in subtraction:
    print(row)    
