import random
list = []
for count in range(1, 11):
	random_num = round(random.random() * 10000)
	list.append(int(random_num))

print "Original, Unsorted List:", list
decrement = 1

print "Computer-Sorted List:", list.sort()
for j in range(1, len(list)):
	for i in range(0, len(list)-decrement):
		if list[i+1]<list[i]:
			temp=list[i]
			list[i]=list[i+1]
			list[i+1]=temp
	decrement+=1

print "Sorted List:", list