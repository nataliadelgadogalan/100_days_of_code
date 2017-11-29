# Objects in python and built in functions
#def add(number_1, number_2):
	#eval('number_1 + number_2')

def add_number(number_list, number_1):
	number_list.append(number_1)
	return number_list

class MyFriends:
	def __init__(self, name, surname, age, number_1, number_2):
		self.name = name
		self.surname = surname
		self.age = age
		self.number_1 = number_1
		self.number_2 = number_2
	
	# functions
	def presentation(self):
		print('Hi! I am %s %s and I am %d years old' % (self.name, self.surname, self.age))
	
# main
a = MyFriends('Peanut', 'Butata', 107, 4, 7)
b = MyFriends('Gus', 'Gus', 17, 19, 34)
c = MyFriends('Fufi', 'Pan', 1070, 22, 65)

a.presentation()
b.presentation()
c.presentation()

number_list = []
number_list = add_number(number_list, a.number_1)
number_list = add_number(number_list, b.number_1)
number_list = add_number(number_list, c.number_1)

print(number_list)

n = list(str(c.number_2))
print(n)
