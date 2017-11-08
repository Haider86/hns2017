import sys

z=1
while(z>0):
    z=z+1
    username=input('enter your user name :')
    if username==('Haider'):
        print('pleas try igen')
    else:z=0
else:z=z+1
P=0 #password part
while (P<3):
    pssw=input('key in your password: ')
    if pssw=="cyber":
        P=3
    else:
        pssw=input('\nWrong password, \nSecond chance: ')
        P=P+1
        if pssw=="cyber":
            P=3
        else:
            pssw=input('\nWrong password, \nWrong again will terminate the program... \nType again: ')
            P=P+1
            if pssw=="cyber":
                P=3
            else:
                print( "Bye...")
                exit('ASGN_1151102784_A01A.py')     #terminate program after 3 error pssw
print ("\nWelcome "+username)
