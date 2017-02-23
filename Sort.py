#Group Nicholas
#CSCI 241 Project 1
#Spring 2017

import random, time, copy

def insertion_sort(arr):
	for k in range(1, len(arr)):
		item_to_place = arr[k]
		j = k
		while j > 0 and arr[j-1] > item_to_place:
			arr[j] = arr[j-1]
			j = j-1
			arr[j] = item_to_place
	return arr

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

#random arrays
array_1000 = []
for i in range (0,1000): 
	array_1000.append(random.randint(-1000,1000)) 
cop_array_1000 = copy.deepcopy(array_1000)

array_2500 = []
for i in range (0,2500): 
	array_2500.append(random.randint(-1000,1000))
cop_array_2500 = copy.deepcopy(array_2500)

array_5000 = []
for i in range (0,5000): 
	array_5000.append(random.randint(-1000,1000))
cop_array_5000 = copy.deepcopy(array_5000)

array_7500 = []
for i in range (0,7500): 
	array_7500.append(random.randint(-1000,1000))
cop_array_7500 = copy.deepcopy(array_7500)

array_10000 = []
for i in range (0,10000): 
	array_10000.append(random.randint(-1000,1000))
cop_array_10000 = copy.deepcopy(array_10000)

#increasing arrays
inc_1000 = []
for i in range(0,1000):
	inc_1000.append(i)

inc_2500 = []
for i in range(0,2500):
	inc_2500.append(i)

inc_5000 = []
for i in range(0,5000):
	inc_5000.append(i)

inc_7500 = []
for i in range(0,7500):
	inc_7500.append(i)

inc_10000 = []
for i in range(0,10000):
	inc_10000.append(i)

#decreasing arrays
dec_1000 = []
for i in range(1000, 0, -1):
	dec_1000.append(i)
cop_dec_1000 = copy.deepcopy(dec_1000)

dec_2500 = []
for i in range(2500, 0, -1):
	dec_2500.append(i)
cop_dec_2500 = copy.deepcopy(dec_2500)

dec_5000 = []
for i in range(5000, 0, -1):
	dec_5000.append(i)
cop_dec_5000 = copy.deepcopy(dec_5000)

dec_7500 = []
for i in range(7500, 0, -1):
	dec_7500.append(i)
cop_dec_7500 = copy.deepcopy(dec_7500)

dec_10000 = []
for i in range(10000, 0, -1):
	dec_10000.append(i)
cop_dec_10000 = copy.deepcopy(dec_10000)

if __name__ == '__main__':
	#1000 random
	insert_start = time.clock()
	insertion_sort(array_1000)
	insert_end = time.clock()
	print('Insert sort 1000 random =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_array_1000)
	selec_end = time.clock()
	print('Selection sort 1000 random =  ' + '{:.20f}'.format(selec_end - selec_start))

	#2500 random
	insert_start = time.clock()
	insertion_sort(array_2500)
	insert_end = time.clock()
	print('Insert sort 2500 random =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_array_2500)
	selec_end = time.clock()
	print('Selection sort 2500 random =  ' + '{:.20f}'.format(selec_end - selec_start))

	#5000 random
	insert_start = time.clock()
	insertion_sort(array_5000)
	insert_end = time.clock()
	print('Insert sort 5000 random =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_array_5000)
	selec_end = time.clock()
	print('Selection sort 5000 random =  ' + '{:.20f}'.format(selec_end - selec_start))

	#7500 random
	insert_start = time.clock()
	insertion_sort(array_7500)
	insert_end = time.clock()
	print('Insert sort 7500 random =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_array_7500)
	selec_end = time.clock()
	print('Selection sort 7500 random =  ' + '{:.20f}'.format(selec_end - selec_start))

	#10000 random
	insert_start = time.clock()
	insertion_sort(array_10000)
	insert_end = time.clock()
	print('Insert sort 10000 random =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_array_10000)
	selec_end = time.clock()
	print('Selection sort 10000 random =  ' + '{:.20f}'.format(selec_end - selec_start))

	#Increasing Arrays
	#1000 Increasing
	insert_start = time.clock()
	insertion_sort(inc_1000)
	insert_end = time.clock()
	print('Insert sort 1000 increase =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(inc_1000)
	selec_end = time.clock()
	print('Selection sort 1000 increase =  ' + '{:.20f}'.format(selec_end - selec_start))

	#2500 inc
	insert_start = time.clock()
	insertion_sort(inc_2500)
	insert_end = time.clock()
	print('Insert sort 2500 increase =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(inc_2500)
	selec_end = time.clock()
	print('Selection sort 2500 increase =  ' + '{:.20f}'.format(selec_end - selec_start))

	#5000 inc
	insert_start = time.clock()
	insertion_sort(inc_5000)
	insert_end = time.clock()
	print('Insert sort 5000 increase =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(inc_5000)
	selec_end = time.clock()
	print('Selection sort 5000 increase =  ' + '{:.20f}'.format(selec_end - selec_start))

	#7500 inc
	insert_start = time.clock()
	insertion_sort(inc_7500)
	insert_end = time.clock()
	print('Insert sort 7500 increase =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(inc_7500)
	selec_end = time.clock()
	print('Selection sort 7500 increase =  ' + '{:.20f}'.format(selec_end - selec_start))

	#10000 inc
	insert_start = time.clock()
	insertion_sort(inc_10000)
	insert_end = time.clock()
	print('Insert sort 10000 increase =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(inc_10000)
	selec_end = time.clock()
	print('Selection sort 10000 increase =  ' + '{:.20f}'.format(selec_end - selec_start))

	#Decreasing Arrays
	#1000 dec
	insert_start = time.clock()
	insertion_sort(dec_1000)
	insert_end = time.clock()
	print('Insert sort 1000 decrease =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_dec_1000)
	selec_end = time.clock()
	print('Selection sort 1000 decrease =  ' + '{:.20f}'.format(selec_end - selec_start))

	#2500 dec
	insert_start = time.clock()
	insertion_sort(dec_2500)
	insert_end = time.clock()
	print('Insert sort 2500 decrease =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_dec_2500)
	selec_end = time.clock()
	print('Selection sort 2500 decrease =  ' + '{:.20f}'.format(selec_end - selec_start))

	#5000 dec
	insert_start = time.clock()
	insertion_sort(dec_5000)
	insert_end = time.clock()
	print('Insert sort 5000 decrease =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_dec_5000)
	selec_end = time.clock()
	print('Selection sort 5000 decrease =  ' + '{:.20f}'.format(selec_end - selec_start))

	#7500 dec
	insert_start = time.clock()
	insertion_sort(dec_7500)
	insert_end = time.clock()
	print('Insert sort 7500 decrease =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_dec_7500)
	selec_end = time.clock()
	print('Selection sort 7500 decrease =  ' + '{:.20f}'.format(selec_end - selec_start))

	#10000 dec
	insert_start = time.clock()
	insertion_sort(dec_10000)
	insert_end = time.clock()
	print('Insert sort 10000 decrease =  ' + '{:.20f}'.format(insert_end - insert_start))
	
	selec_start = time.clock()
	selection_sort(cop_dec_10000)
	selec_end = time.clock()
	print('Selection sort 10000 decrease =  ' + '{:.20f}'.format(selec_end - selec_start))


