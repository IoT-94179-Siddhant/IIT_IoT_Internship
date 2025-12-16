#simple and clear version
def overlapping(list1,list2):
    for item in list1:
        if item in list2:
            return True
        return False
    
#using sets
def overlapping(list1,list2):
    return bool(set(list1)& set(list2))

#main code
print(overlapping([1,2,3],[1,2,3]))  #True
print(overlapping([10,20,30],[300,40,50]))  #False