# This Quiz is to help me with my Microsoft Azure Certification
# In the quiz I will be asking for different categories of cloud



print("Welcome to my Azure quiz.")

playing = input('Do you want to play? ') #This is to just introduce the quiz to the user 

if playing.lower() != "yes":
    quit() #If the user does not type yes it will stop the program 

print("Lets play!!")
score = 0 # This quiz will also keep score I have done this by creating a score variable to store the integer 

answer = input("what does SaaS mean? ")
if answer.lower() == "Software as a service": 
    print('correct!!')
    score += 1 #Adds 1 if correct 
else:
    print('incorrect')


answer = input("what does PaaS mean? ")
if answer.lower() == 'Platform as a service': # I used .lower() function to bring what ever answer the user types to lowercase
    print('correct!!')
    score += 1
else:
    print('incorrect')

answer = input("what does IaaS mean? ")
if answer.lower() == 'Infrastructure as a service': 
    print('correct!!')
    score += 1
else:
    print('incorrect')


print("You got" + str(score)+ " questions correct!") # This displays the code 
print("You got " + str((score / 4) * 100) + "%.") # This creates a percentage for the user