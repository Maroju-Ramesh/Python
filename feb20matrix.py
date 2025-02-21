# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# def print_matrix(list):
#     for i in range(len(list1)):
#         for j in range(len(list1)):
#             print(list1[i][j], end="")
#         print()
# print_matrix(list1)

# #two diagonals addition
# sum =0
# for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             if i==j or i+j == len(list1)-1:
#                 sum+=list1[i][j]
#                 #for adding 5 two times as it is common for both diagonals
#                 if i==j and i+j == len(list1)-1:
#                  sum+=list1[i][j]
# print(sum)


list2 = [[1,2,3,4],
         [5,6,7,8],
         [4,5,6,7],
         [1,3,4,5]]
def print_matrix(list):
    for i in range(len(list2)):
        for j in range(len(list2)):
            if (i==0 or j==0) or (i==len(list2)-1 or j==len(list2)-1): 
              print(list[i][j], end="")
            else:
                print(" ", end="")
        print()
    
print_matrix(list2)