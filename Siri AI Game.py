from __future__ import print_function
import random
def textgame():
    print ("What is your name?")
    name = str(raw_input('User Name: '))
    print ("Hello " + name + "! My name is Siri. I will be acting as your virtual assistant in this activity. Would you like to play a game?")
    r1 = str(raw_input('Y/N: '))
    a1 = ('Y') or ('y')
    while r1 == a1:
        print ("OK")
        break
    else:
        print ("Maybe another time then.")
    print ("What is 100000*3?")
    r2 = str(raw_input('Answer: '))
    a2 = ('300000')
    while r2 == a2:
        print ('Correct!')
        break
    else:
        print ('Wrong answer.')
    print ('Let\'s try something a little more visual.')
    
    
    