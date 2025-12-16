#given tuple of tuples
data=(
    (10,10,10,12),
    (30,45,56,45),
    (81,80,39,32),
    (1,2,3,4)
)

#number of rows
rows=len(data)

#calculate column wise average
averages=[]
for col in range(len(data[0])):
    column_sum=0
    for row in data:
        column_sum+=row[col]
    averages.append(column_sum/rows)

#output
print(averages)    