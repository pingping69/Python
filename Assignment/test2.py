list1 = ['1','2','3']
list2 = ['a','b','c']

list3 = [1,2,3,4,5,6,7,8]

new_list = list(map((lambda x:x<5),list3))

def gen():
	return "List1",list1,"List2",list2
