import datetime


def getdate():

	# to get date and time
	return datetime.datetime.now()

def selectname():
	
	name = {1: "Shivam", 2: "ojas"}
	b = {1: "Food", 2: "Exercise"}
	
	for key, value in name.items():

		# taking input of name
		print("Press", key, "for", value, "\n", end="")
		
	n = int(input("type here.."))
	
	if n > 2:
		print("error select 1 or 2")
		exit()
	else:
		return n


def select_file_action():
	
	a = {1: "Log", 2: "Retrieve"}
	
	for key, value in a.items():

		# taking input of function that user wants to
		# do (either log or retrieve)
		print("Press", key, "for", value, "\n", end="")

	x = int(input("type here.."))
	
	if x > 2:
		print("error select 1 or 2")
		exit()
	else:
		return x


def select_task():
	
	b = {1: "Food", 2: "Exercise"}
	
	for key, value in b.items():
		
		# ask user to choose between food
		# and exercise
		print("Press", key, "for", value, "\n", end="")

	y = int(input("type here.."))
	
	if y > 2:
		print("error select 1 or 2")
		exit()
	else:
		return y


def action(n, x, y):
	
	# condition no 1
	if n == 1 and x == 1 and y == 1:
		value = input("type here\n")

		with open("shivam food.txt", "a") as shivamfood:

			# printing date and time
			shivamfood.write(str([str(getdate())]) + ": " + value + "\n")
			print("successfully written")

	# condition no 2
	elif n == 1 and x == 1 and y == 2:
		value = input("type here\n")

		# printing date and time
		with open("shivam exercise.txt", "a") as shivamexercise:

			# printing date and time
			shivamexercise.write(str([str(getdate())]) + ": " + value + "\n")
			print("successfully written")

	# condition 3
	elif n == 2 and x == 1 and y == 1:
		value = input("type here\n")

		# printing date and time
		with open("ojas food.txt", "a") as ojasfood:

			# printing date and time
			ojasfood.write(str([str(getdate())]) + ": " + value + "\n")
			print("successfully written")

	# condition 4
	elif n == 2 and x == 1 and y == 2:
		value = input("type here\n")

		# printing date and time
		with open("ojas exercise.txt", "a") as ojasexercise:

			# printing date and time
			ojasexercise.write(str([str(getdate())]) + ": " + value + "\n")
			print("successfully written")

	# condition 5
	elif n == 1 and x == 2 and y == 1:

		# printing date and time
		with open("shivam food.txt", "r") as shivamfood:
			a = shivamfood.read()
			print(a)

	# condition no 6
	elif n == 1 and x == 2 and y == 2:

		# printing date and time
		with open("shivam exercise.txt", "r") as shivamexercise:
			a = shivamexercise.read()
			print(a)

	# condition no 7
	elif n == 2 and x == 2 and y == 1:

		# printing date and time
		with open("ojas food.txt", "r") as ojasfood:
			a = ojasfood.read()
			print(a)

	# condition no 8
	elif n == 2 and x == 2 and y == 2:

		# printing date and time
		with open("ojas exercise.txt", "r") as ojasexercise:
			a = ojasexercise.read()
			print(a)

n = selectname()
x = select_file_action()
y = select_task()
action(n, x, y)


