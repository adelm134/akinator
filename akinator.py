def restart():
    answers = []
    intro()
    game()
    score()
    result()
    outro()

def intro():
    start = 'Welcome to Akinator! Think about a real person in COM. I will try to guess who it is :>'
    tip = 'Answer the questions with Yes or No.'
    begin = 'Ready? The first question is...'

def game():
    questions = ['Is this person a woman?', "Is this person's hair long?", "Is this person a student?", "Does this person watch anime?", "Is this person kyrgyz?", "Does this person wear glasses?", "Is this person cringe?"]
    for question in questions:
        if reply == 'Yes':
            answers.append(reply)
        elif reply == 'No':
            answers.append(reply)
        else:
            print('Please answer with Yes or No! >:(')

def results():
	if answer == Alymbek:
		print ("We guess this person is Alymbek.") 
	elif answer == Dovlyat:
		print ("We guess this person is Dovlyat.")
	elif answer == miss Burul:
		print ("We guess this person is miss Burul.")
	elif answer == Ruslan Isaev:
		print ("We guess this person is Ruslan Isaev.")
	elif answer == Abiy:
		print ("We guess this person is Abiy.")
	elif answer == Kurstan:
		print ("We guess this person is Kurstan.")
	elif answer == Sae Yeon:
		print ("We guess this person is Sae Yeon.")
	elif answer == Erik:
		print ("We guess this person is Erik.")
	elif answer == Sotomura:
		print ("We guess this person is Sotomura.")
	elif answer == Zhumaniiaz Mamataliev:
		print ("We guess this person is Zhumaniiaz Mamataliev.")
	elif answer == grey:
		print ("We guess your color is grey.")
	elif answer == silver:
		print ("We guess your color is silver.")
	elif answer == gold:
		print ("We guess your color is gold.")
	elif answer == magenta:
		print ("We guess your color is magenta.")
	else: #If the answer list does not match ANY of the colors
		print ("Your color is too hard or doesnt even exist. We couldn't guess it. Play again!")