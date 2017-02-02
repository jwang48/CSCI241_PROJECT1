import random

array = []
for i in range (0,10):
	array.append(random.randint(-50,50))

def insertion_sort(arr):
	for k in range(1, len(arr)):
		item_to_place = arr[k]
		j = k
		while j > 0 and arr[j-1] > item_to_place:
			arr[j] = arr[j-1]
			j = j-1
		arr[j] = item_to_place


sort_me = [9,8,7,6,5,4,4,2,1,5,6,7,31,9,753,12]

# insertion_sort(sort_me)
# print(sort_me)

testeasy = [5,3,1,6]

def selection_sort(arr):
	for k in range(0, len(arr)):

		smallest = arr[k]
		j = k+1
		while j < len(arr):
			if smallest >= arr[j]:
				temp = smallest
				smallest = arr[j]
				arr[k]= smallest
				arr[j] = temp
			j+=1
	return arr

#print ("RESULT " + str(selection_sort(testeasy)))
#print ("RESULT " + str(selection_sort(sort_me)))
print ("RESULT " + str(selection_sort(array)))

