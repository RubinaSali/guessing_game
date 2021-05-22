import random
ran_num= random.randint(1,10)

while True:
	x = int(input("guess "))
	if x<ran_num:
		print("your guess is too low , u lost")
	elif x>ran_num:
		print("your guess is too high , u lost")
	else:
		print("your guess is right, you won!!")
		#play again
		play_again = input("do you want to continue? y/n ")
		if play_again== "y":
			x = None
			ran_num= random.randint(1,10)
		else:
			print("Thank you for playing")
			break
