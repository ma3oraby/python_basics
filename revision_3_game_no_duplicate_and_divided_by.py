'''
Game : 
    -start --> welcome msg 
    - choices --> enter game number 
    - start game : divided by [1:1oo] , sentence no duplicate
    - end --> ask play again
    - choices : y or n
    - n : exit game 
    - y : choice play again  

'''

class Game : 

    def __init__ (self) :
        while True :
            print (''' Welcome .. 
            Choose a game 
            1 for Divided By game
            2 for No Duplicate game ''')
            user_choice = int(input("Enter Game Number : "))

            if user_choice == 1 : 
                x = int(input("Enter first number : "))
                y = int(input("Enter last number : "))
                self.divided_by(x,y)

            elif user_choice == 2 : 
                sentence = input ("enter a sentence :")
                self.no_duplicate (sentence)
            play_again = input ("press y to play again , n to exit : ")
            if play_again == "n" : 
                print ("Goodbye")
                break

        
    def divided_by (self,x,y):

        for n in range (1,101):
            if n%x==0 and n%y==0 :
                print (n)

    def no_duplicate (self , sentence) :
        words = []
        for x in sentence.split(" ") : 
            if x not in words : 
                words.append(x)
        print (' '.join (words))


player_1 = Game ()



