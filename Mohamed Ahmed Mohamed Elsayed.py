# def selection(arr):
#     num = len(arr)
#     for i in range(num - 1):
#         x = i
#         for j in range(i + 1, num):
#             if arr[j] < arr[x]:  
#                 x= j 
        
#         arr[i], arr[x] = arr[x], arr[i]

# arr = [ 70 , 85 , 12 , 22 , 11 , 5 , 1 ]
# selection(arr)
# print("Sorted array:", arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
    return arr

arr = [10,5,14,8,4,20,25]
sorted_arr = insertion_sort(arr)
print(sorted_arr)