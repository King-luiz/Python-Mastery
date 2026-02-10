#for loops

for number in range(3,10,2):
    print("Attempt", number+1, (number+1)*"*")
    
    
  
print("      ")    
# fo...else
successful = False
for number in range(3):
    print("Attempt") 
    if successful:
        print("Successful")
        break 
else:
    print("Attempted 3 times and failed")



#nested loops

print("                ")
#loops inside other loops


for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


print("                ")
#iterables
print(type(6))
print(type(range(5)))
for x in "Python":
    print(x)
    
print("                ")


shopping_cart = ["milk", "bread", "eggs"]
for items in shopping_cart:
     print(items)   
     
     
     
     
   
print("                ")     
#while loops


number = 100
while number > 0:
    print(number)
    number //= 2     
    
    
    
# run in terminal to stop the loop    
# print("          ") 
# command = " "
# while command != "quit" and command != "QUIT":
#     command = input(">")
#     print("ECHO", command)


# infinite loops

#runs forever

# command = " "
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break