# def find_max(list):
#     max = float("-inf")
#     for i in list:
#         max = i if i > max else max
#     return max

# list1=[[2,3,1],[2,3,4],[5,4,3]]
# res=[]
# for j in list1:
#     res.append(find_max(j))
# print(res)


#---------Binary search - It can be perfromed only on a sorted list-------
# search_element = int(input("Enter number to search"))
# list1 = [1 , 2, 10, 32, 75, 89, 100]
# low = 0
# high = len(list1) - 1


# flag = False
# while low <= high:
#     mid = int((low + high)/ 2)
#     if list1[mid] == search_element:
#         flag = True
#         print(mid)
#         break
#     elif list1[mid] > search_element:
#         high = mid - 1
#     else:
#         low = mid + 1


# if flag == False:
#     print("Not found")
 #----------------binary search ---using function----------

def binary_search(list1, search_element):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = int((low + high)/ 2)
        if list1[mid] == search_element:
            return mid
        elif list1[mid] > search_element:
            high = mid - 1
        else:
            low = mid + 1
    return -1

list2 = [1 , 2, 10, 32, 75, 89, 100]

res = binary_search(list2, search_element)

if res != -1:
    print(res)
else:
    print("Not found")
