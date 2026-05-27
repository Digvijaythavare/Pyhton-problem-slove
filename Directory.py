import os
import time

print("This is cureent working directory:\n",os.getcwd())
time.sleep(2)
print("Now we will change the current working directory: ")
time.sleep(2)
print("This is change directory",os.chdir("D:\\Program"))
print(os.getcwd())
time.sleep(2)
print("There is list of all directory",os.listdir())
time.sleep(2)   
print("We can creater new directory in current directory : ",os.mkdir("Program"))
time.sleep(2)
print("Here is list of new directory: ",os.listdir())