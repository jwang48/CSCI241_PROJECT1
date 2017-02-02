def insertion_sort(arr):
      for k in range(1, len(arr)):
           item_to_place = arr[k]
           j=k
           while j > 0 and arr[j-1] > item_to_place:
                    arr[j] = arr[j-1]
                    j = j-1
           arr[j] = item_to_place