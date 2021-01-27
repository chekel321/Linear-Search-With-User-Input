# create a function that looks a through a list and finds the input number
import time
key = int(input("enter a number: "))
list = [1,3,4,5,6,55,67,887,123]


def found_it(list, key):
   x = True
   while x:
      index = 0 
      found = False
      time.sleep(.5)
      while index < len(list) and not found:
         if list[index] == key:
            found = True
            

         else:
            print("not found on index: ", index)
            index += 1
         time.sleep(.5)
      if found == True:
         print(key, " is found at index ", index)

      else:
         print(key, "not found")

      again = input("would you like to try again y/n: ")
      if again == "y":
         key = int(input("enter a number: "))
         continue
      else:
         print("thank you for playing")
         break

      
found_it(list, key)
