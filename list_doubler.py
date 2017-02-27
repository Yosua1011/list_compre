my_list = [21, 2, 93]

def list_doubler(lst):
	doubled = [num * 2 for num in lst]
	return doubled

my_doubled_list = list_doubler(my_list)
print my_doubled_list