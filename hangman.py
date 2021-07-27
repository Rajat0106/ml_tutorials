import random
#random.seed(42)

points=100
with open("words_medium.txt") as f :
    words=f.readlines()
    
new_words=[]
for word in words[:-1] :
    new_words.append(word[:-1])


choice= random.choice(words) ##wires
#print (choice)
print(choice[0]) ##w


for i in range(1, len(choice)-1):   
    user_char=input("Enter next character: ")
    
    if user_char==choice[i]: ##correct choice case
        print(f"Current points are: {points}")
        
    else: ##incorrect case
        points = points//2
        print("Incorrect choice")
        print(f"The correct character is: {choice[i]}")
        print(f"Current points are: {points}")
        
        













    
    
##idx = 1
##def correct(idx):
##    print("correct")
##    user_char=input("Enter next character: ")
##    correc
##    idx+=1    
##
##def hm():
##    choice= random.choice(words)
##    print(choice[0])
##    if user_char==choice[idx]:
##        correct(idx)
##        
##    else:
##        print ("Incorrect")
##        
##
##hm()
