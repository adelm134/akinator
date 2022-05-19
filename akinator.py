def restart():
    answers = []
    intro()
    game()
    scoring()
    result()
    outro()

def intro():
    start = 'Welcome to Akinator! Think about a real person in COM. I will try to guess who it is :>'
    tip = 'Answer the questions with Yes or No.'
    begin = 'Ready? The first question is...'

def game():
    questions = ['Is this person a woman?', "Is this person's hair long?", "Is this person a student?", "Does this person watch anime?", "Is this person kyrgyz?", "Does this person wear glasses?", "Is this person cringe?"]
    for question in questions:
        if reply == 1:
            answers.append(reply)
        elif reply == 2:
            answers.append(reply)
        else:
            print('Please answer with 1 as Yes or 2 as No! >:(')

def results():
	if answer == Alymbek:
		print ("We guess this person is Alymbek.") 
	elif answer == Dovlyat:
		print ("We guess this person is Dovlyat.")
	elif answer == Burul:
		print ("We guess this person is miss Burul.")
	elif answer == Ruslan:
		print ("We guess this person is Ruslan Isaev.")
	elif answer == Abiy:
		print ("We guess this person is Abiy.")
	elif answer == Kurstan:
		print ("We guess this person is Kurstan.")
	elif answer == SaeYeon:
		print ("We guess this person is Sae Yeon.")
	elif answer == Erik:
		print ("We guess this person is Erik.")
	elif answer == Sotomura:
		print ("We guess this person is Sotomura.")
	elif answer == ZhumaniiazMamataliev:
		print ("We guess this person is Zhumaniiaz Mamataliev.")
	elif answer == Adel:
		print ("We guess this person is Adel.")
	elif answer == Akylai:
		print ("We guess this person is Akylai.")
	elif answer == Aruuke:
		print ("We guess this person is Aruuke.")
	elif answer == Aliia:
		print ("We guess this person is Aliia.")
	else: 
		print ("Your person is too hard or doesnt even exist. We couldn't guess it. Play again!")

def outro():
	thanks = "Thank you for playing our game! We hope you liked it! ❤"
	repeat = "Want to play again?"
	bye = "Goodbye!! Come again soon!"
	
#MAIN	
#initialize variables
Alymbek = [2, 2, 1, 1, 1, 2, 2] 
Dovlyat = [2, 2, 1, 2, 2, 1, 2]
Burul = [1, 1, 2, 2, 1, 2, 2]
Ruslan = [2, 2, 2, 1, 2, 2, 2]
Abiy = [2, 2, 1, 1, 1, 2, 2]
Kurstan = [2, 2, 1, 1, 1, 1, 2]
SaeYeon = [1, 1, 1, 1, 2, 2, 2]
Erik = [2, 2, 1, 1, 2, 1, 2]
Sotomura = [2, 2, 1, 1, 2, 2, 1]
ZhumaniiazMamataliev = [2, 2, 2, 2, 1, 1, 2]
Adel = [1, 1, 1, 1, 1, 1, 2]
Akylai = [1, 2, 1, 1, 1, 2, 2]
Aruuke = [1, 1, 1, 2, 1, 2, 2]
Aliia = [1, 1, 1, 1, 1, 2, 2]  
answer = []

#begin program
intro()
game()
results()
