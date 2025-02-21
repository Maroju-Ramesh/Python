

#sum of outer box of a matrix
list2 = [[1,2,3,4],
         [5,6,7,8],
         [4,5,6,7],
         [1,3,4,5]]
def print_matrix(list):
    sum=0
    for i in range(len(list2)):
        for j in range(len(list2)):
            if (i==0 or j==0) or (i==len(list2)-1 or j==len(list2)-1): 
              sum+=list[i][j]
              
    print(sum)    
print_matrix(list2)