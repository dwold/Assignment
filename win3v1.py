mport random


def hand_game():
    form = ['Rock','Paper','Scissors']
    com_form = random.choice(form)
    print ('Welcome to Rock-Paper-Scissors Game!')
    usr_form = input('Please choose 1-3 for:\n 1 - rock\n 2 - paper\n 3 - scissors\n')
    while usr_form != '1' and usr_form != '2' and usr_form != '3':
        usr_form = input('Wrong key please enter numbers 1-3\n')
    x = form.index(com_form) + 1
    y = int(usr_form)
    if x-y == 0:
        print('Computer\'s form was also {}, please try again!\n'.format(com_form))
        hand_game()
    elif x-y == -1 or x-y == 2:
        print('Computer\'s form was {}, You Win!\n'.format(com_form))
    else:
        print('Computer\'s form was {}, You Loose!\n'.format(com_form))
hand_game()
