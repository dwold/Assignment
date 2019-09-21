import random


class Description:
    
    def __init__(self):
        self.desc1 = 'Empty room.'
        self.desc2 = 'You have got a passcode.'
        self.desc3 = 'You have got a key.'
        self.desc4 = 'You have got a safe box.'
        self.desc5 = 'You have got a magnet.'
        self.all_desc = [self.desc1,self.desc2,self.desc1,self.desc3,self.desc1,self.desc4,self.desc5]
        self.rooms = ['1','2','3','4','5','6','7']
        self.room_desc = {}
        
    def asgn_room(self): 
        random.shuffle(self.rooms)
        for i in range (7):
            room = self.rooms[i]
            desc = self.all_desc[i]
            self.room_desc[room] = desc


class Game:
    
    def __init__(self):
        self.checked_rooms = []
        self.description = Description() 
        self.empty_room = self.description.desc1
        self.opt = None 
        self.show = None 
        self.point = 0
        self.loss = 0
        self.score = 0
        print('''Welcome to Adventure Game!\nIn this game you need to explore seven rooms numbered from \'1\' to \'7\'.
                 \nThe goal is to get a safe box, a magnet, a passscode and a key. Once you had seen a room you cannot go again.\n''')
        self.description.asgn_room() 
        self.usr_inpt() 


    def usr_inpt(self):
        self.opt = input ('''Where do you want to go?
                            \nPress a number  of your choice \'1\' - \'7\' or press \'q\' to quit the game.\n''')
        while self.opt not in ['1','2','3','4','5','6','7','q']:
            self.opt = input ('Wrong key, please try again.')

        if self.opt == 'q':
            print ('Goodbye!')
        else:
            self.show = self.description.room_desc.get(self.opt) 
            self.play_game()


    def play_game(self):
        if self.opt in self.checked_rooms:
            self.loss -= 10
            
        if self.show != self.empty_room:                   
            self.point += 1
        else:
            self.loss -= 1
            
        self.checked_rooms.append(self.opt)
        self.print_out(self.opt)
                                               
        if self.point+self.loss < -1:
            self.end_game(0)
        elif self.point == 4:
            self.end_game(1)
        else:
            self.usr_inpt()


    def print_out(self,key):
        self.key = key
        self.score = int((self.point + self.loss)*25)
        print(self.show, '\nPoint: {}\n'.format (self.score))

                
    def end_game(self,code):
        self.code = code
        self.score = int((self.point + self.loss)*25)

        if self.code==1:
            print('Congratulations! You Won!')
        else:
            print('Gameover, you lost the game.')


game = Game()
