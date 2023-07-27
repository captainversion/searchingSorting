 
##  1.Implement Binary Search

# def binary_search(arr, low, high, x):
#     if high >= low:
#         mid = (high + low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x) 
#         else:
#             return binary_search(arr, mid + 1, high, x)
#     else:
#         return -1
 
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
# result = binary_search(arr, 0, len(arr)-1, x) 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")

##-------------------------------------------------------------------------------------------------------------------------------

## 2.Implement Merge Sort

# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#     L = [0] * (n1)
#     R = [0] * (n2)
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#     i = 0     
#     j = 0     
#     k = l     
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
 
# def mergeSort(arr, l, r):
#     if l < r:
#         m = l+(r-l)//2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m+1, r)
#         merge(arr, l, m, r)
 
# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ") 
# mergeSort(arr, 0, n-1)
# print("\n\nSorted array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ")

##-----------------------------------------------------------------------------------------------------------------------------------

## 3.Implement Quick Sort

# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low, high):
#         if array[j] <= pivot:
#             i = i + 1
#             (array[i], array[j]) = (array[j], array[i])
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
#     return i + 1

# def quickSort(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         quickSort(array, low, pi - 1)
#         quickSort(array, pi + 1, high)
  
# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data) 
# size = len(data) 
# quickSort(data, 0, size - 1) 
# print('Sorted Array in Ascending Order:')
# print(data)

##------------------------------------------------------------------------------------------------------------------------------------

## 4.Implement Insertion Sort

# def insertionSort(arr):
     
#     if (n := len(arr)) <= 1:
#       return
#     for i in range(1, n):
         
#         key = arr[i]
#         j = i-1
#         while j >=0 and key < arr[j] :
#                 arr[j+1] = arr[j]
#                 j -= 1
#         arr[j+1] = key

# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print(arr)

##--------------------------------------------------------------------------------------------------------------------------------

## 5.Write a program to sort list of strings (similar to that of dictionary)

# def sort_strings(strings):
#     string_dict = {s: None for s in strings}
#     sorted_keys = sorted(string_dict.keys())
#     sorted_strings = [key for key in sorted_keys]
#     return sorted_strings

# strings = ["apple", "banana", "cat", "dog", "elephant"]
# sorted_strings = sort_strings(strings)

# print("Sorted list based on dictionary-like ordering:", sorted_strings)
