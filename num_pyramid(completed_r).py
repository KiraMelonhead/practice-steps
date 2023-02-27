x = input()
arg = 1
while int(arg) <= int(x):
	com = str(str(arg) * int(arg))
	if len(com) != arg:
		print(com[:arg])
	else:
		print(str(arg) * int(arg))

	arg = int(arg) + 1

# The story of this code.
# The idea of this code is just to print pyramid of numbers, that has have been inputted by user.
# The height and width are accorded by the number; higher number means higher pyramid.
# First the code was just all above the while statement and two lines after: line 8 and line 10.
# And it was working. right before 10.
# After 10 and farther increasing in the numbers digits the look of the pyramid had been getting disordered.
# First I tried to solve this misunderstanding by catching dividable to 10 numbers by %10 but
# soon realized that was a bad idea; I had have been to catch all 2 and above digit number
# by adding additional if statement. It was not the way.
# My saviour showed up in the face of the len() function and lists.
# All I had to do was to compare the length of the list to the value of 'arg' and cut
# the needed length of the list.

# The end.
