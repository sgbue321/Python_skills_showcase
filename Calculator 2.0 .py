

num_1 = int(input("Type in a number: ")) 
num_2 = int(input("Type in another number: "))

#these two variable inputs ask the user to type in numbers and the "int" specifies it as a integer
print("choose Calculation : ",
      "Add ",
      "Subtract ",
      "Multiply ",
      "Divide ")
#These show what calculations the user can use 
calc = input()

if calc == "Add":
    print (num_1 + num_2)
elif calc == "Subtract":
   print (num_1 - num_2)
elif calc == "Multiply":
    print (num_1 * num_2)
elif calc == "Divide":
    print (num_1 / num_2)





