list_2=sorted(list_1)
# res=[]
# for i in list_1:
#     temp=list_2.index(i) +1
#     res.append(temp)
# print(list_2)
# print(res)


# list_1=[10,8,7,1,6,5,9]
# list_1.sort()
# low=len(list_1)//2
# high=len(list_1) -1
# while(low<high):
#     list_1[low],list_1[high]=list_1[high],list_1[low]
#     low+=1
#     high-=1
# print(list_1)


# list_1=[[1,4,5,6],[3,6,7,5],[7,0,22,90]]
# sum=0
# for i in list_1:
#     for j in i:
#         sum+=j
# print(sum, end=" ")


# list_1=[[1,2,3],[2,3,4],[3,4,5]]
# sum=0
# for i in range(len(list_1)):
#     for j in range(len(list_1[i])):
#         if i == 0 or i == len(list_1) - 1:
#             sum += list_1[i][j]
#         elif j==0 or j==len(list_1) -1 :
#             sum+=list_1[i][j]
# print(sum)

# def diagonal_sum(matrix):
#     n = len(matrix)
#     total_sum = 0
#     for i in range(n):
#         total_sum += matrix[i][i]  # Primary diagonal
#         total_sum += matrix[i][n - 1 - i]  # Secondary diagonal
#     return total_sum
#
# # Example
# matrix = [[1, 2, 3], [1, 3, 5], [2, 3, 5]]
# result = diagonal_sum(matrix)
# print(result)  # Output: 17