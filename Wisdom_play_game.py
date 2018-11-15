
# Levels of Game:
# The wisdom source: https://www.salesforce.com/blog/2014/12/words-wisdom-from-two-visionaries.html & https://quotefancy.com/quote/758295/Ralph-Waldo-Emerson-The-invariable-mark-of-wisdom-is-to-see-the-miraculous-in-the-common

Easy_Level = "The two most important ___1___ in your life are the day you ___2___ , and the day you find out ___3___ , The writer name is ___4___"

Normal_Level = "We make a ___1___ by what we ___2___. We make life by what we ___3___, The writer name is ___4___"

Hard_Level = " The ___1___ mark of ___2___ is to see the ___3___ in the common , The writer name is ___4___"




#Game ANSWERS

#easy Level: 1 = days , 2 = born , 3 = why , 4 = Mark Twain , 
#Normal Level: 1 = living , 2 = get , 3 = give , 4 = Winstone Churchill , 
#Hard Level: 1 = invariable , 2 = wisdom, 3 = miraculous , 4 = Ralph Waldo Emerson , 


easy_Answers = [['___1___', 'days'],
               ['___2___', 'born'],    
               ['___3___', 'why'],
               ['___4___' , 'Mark Twain' ]]


Normal_Answers = [[ '___1___' , 'living'],
                 ['___2___'  , 'get' ],                  
                 ['___3___'  ,'give' ],
                 [ '___4___' , 'Winstone Churchill']]



hard_Answers = [['___1___'  , 'invariable'],                
               ['___2___'  , 'wisdom'],                
               ['___3___'  , 'miraculous'],
               ['___4___ ' , 'Ralph Waldo Emerson']]




#The steps will be:

# checks to see if the user answers for the first blank is correct,

#if the answer is correct : The Program will replace the blank by the user answer automatically then it will move the user to the second blank ,

#if the answer is not correct : the user has 5 attempts to try again & also there is a hint to help him.

''' the Lost(attempts) for giving the result if the attempt is over , no return , the function will close the window.. '''


def Lost(attempts):
    
       print "you lost, Try Again"
       exit(0)

''' Here to define a function Blank_Question wich is the blanks we need the user to fill.
answers : is the user input ...
answer_string: is the wisdom with the blank which will print first when the user select the Level ...
it will return to the next step which is replacing the output in the string..

'''
        
           
def Blank_Question(answers, answer_string):

    print answer_string
    
     # here the attmept as the user needs to fill.
    print ""
    attempts = raw_input('Challenge yourself and add the attempt you need to fill overall the 4 blanks: ')
    print ""
 # here is giving the user an infromation before asking him to add the needed value.   
    answer = raw_input('Guess the  ' + answers[0][0] + '   ')

    
    while attempts > 1 and answer != answers[0][1]:
          attempts = int(attempts) - 1 
          print ' '
          print 'You still have', str(attempts) + " attempts"
          print ' '
          answer = raw_input('Try again: Hint: To help you in Guessing, Select from the following (days \ living \ invariable) ')
          if int(attempts) == 1:
             return Lost(attempts)
       
    if answer == answers[0][1]:

    
       answer = raw_input('Guess the ' + answers[1][0] + '   ') # To Add the second blank


    while attempts > 1 and answer != answers[1][1]: 

        attempts = int(attempts) - 1 
        print ' '
        print 'You still have', str(attempts) + " attempts"
        print ' '
        answer = raw_input('Try again: Hint: To help you in Guessing, Select from the following (born \ get \ wisdom) ')
        if int(attempts) == 1:
           return Lost(attempts)

           
    if answer == answers[1][1]:

    
       answer = raw_input('Guess the ' + answers[2][0] + '   ')    # To Add the third blank


    while attempts > 1 and answer != answers[2][1]:

        attempts = int(attempts) - 1 
        print ' '
        print 'You still have', str(attempts) + " attempts"
        print ' '
        answer = raw_input('Try again: Hint:to help you in Guessing, Select from the following (why \ give \ miraculous) ')
        if int(attempts) == 1:
             return Lost(attempts)
           
    if answer == answers[2][1]:
 

       answer = raw_input('Guess the ' + answers[3][0] + '   ')  # To Add the fourth blank


    while attempts > 1 and answer != answers[3][1]:

        attempts = int(attempts) - 1 
        print ' '
        print 'You still have', str(attempts) + " attempts"
        print ' '
        answer = raw_input('Try again: Hint:to help you in Guessing, Select from the following (Mark Twain \ Winstone Churchill \ Ralph Waldo Emerson) ')
        if int(attempts) == 1:
             return Lost(attempts)
           
    if answer == answers[3][1]:

        return replace_Blank_Question(answers, answer_string)
'''
This function for replacing the blank with the user input.
Answer = user input ...

wisdom_string = the exact wisdom sentence which i will compare the user input with...

it's not written above but the computer autmoaticly process it and find it based in my answer_string + Answers for the levels
will return the full wisdom (string)
'''

def replace_Blank_Question(answers, wisdom_string):

    wisdom_string = wisdom_string.split()

    replaced = []
    
#here the computer will check the useer answers with the actual answers then will replace it with the user input..

#then all will be added to the answer string '''

    for word in wisdom_string:

        if answers[0][0] in word:

           word = word.replace(answers[0][0], answers[0][1])
            
        if answers[1][0] in word:

           word = word.replace(answers[1][0], answers[1][1]) 
              
        if answers[2][0] in word:

           word = word.replace(answers[2][0], answers[2][1]) 

        if answers[3][0] in word:

            word = word.replace(answers[3][0], answers[3][1])

            replaced.append(word)

        else:

              replaced.append(word)

        answer_string = ' '.join(replaced)
    print ""
    print "*****"
    print ""
    print "You Got it, The Wisdom is "
    print ""
    print ""
    print answer_string
    print ""
    print "Thank you for playing the game "
    



## here, it's the 1st thing to be shown in the page. 



print ' X ~ X'

print 'Hiiiiii.... welcome To Guess Game. I hope you will enjoy the wisdom game'.title()
print ''
print 'Game instructions:'.upper()
print ''    
print 'Fill the blank & Complete the wisdom & Guess the Writer name'.title()

print ''                    


                                                     
## The 1st page and the options are down in the Coding because we need 1st to define the Variables (Blank_Question) then the function will work.



Welcome_page = raw_input('challenge yourself and select a level (For \ easy press 1 ,medium press 2 , hard press 3): '.title())  
    
if Welcome_page == '1':

   print Blank_Question(easy_Answers, Easy_Level)

   print ' '

elif Welcome_page == '2':

    print Blank_Question(Normal_Answers, Normal_Level)
   
    print ' '

elif Welcome_page == '3':

     print Blank_Question(hard_Answers, Hard_Level)
          
else:
       
     print ("Open the Game Again if you want to play , Bye Bye")
        

          
import turtle
import Tkinter

#below will keep the window open :) I searched about it and its from https://intellij-support.jetbrains.com/hc/en-us/community/posts/206408199-Keeping-Python-Turtle-Graphics-window-open

fred = turtle.Pen()
fred.shape("turtle")
fred.forward(100)
fred.circle(100)
fred.color("blue")
fred.circle(-100)
fred.forward(100)
Tkinter.mainloop()
    
    

    
