print('welcome to my game!!')

playing = input('Do you want to play my game?: ')

if playing != "yes":
    quit()

else:
    print("Let's play")
score = 0 

answer1 = input('What does SaaS mean?: ').lower()

if answer1 == 'Software as a service':
    print('well done!!')
    score += 1 
else:
    print('incorrect try again!')

answer2 = input("What does PaaS mean?: ").lower()

if answer2 == ('Platform as a service '):
    print("That answer is correct!! ")
    score += 1 
else:
    print ("Sorry that's not right!! ")

answer3 = input("What does IaaS mean?: ").lower()

if answer3 == ('Infrastructure as a service '):
    print("That answer is correct!! ")
    score += 1 
else:
    print ("Sorry that's not right!! ")

print ("you got " + str(score) + 'questions correct')  
print("Thank you for taking the Quiz!! ")                           
