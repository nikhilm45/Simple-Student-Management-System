import os
import platform

global listStd 
listStd = ['Nikhil','Aniket'] 

def Student(): 

	x = "#" * 30
	y = "=" * 28
	global bye #Making Bye As Super Global Variable
	bye = "\n BY NIKHILKUMAR MARATHE".format(x, y, y, x) # Will Print GoodBye Message

	#Printing Welcome Message And options For This Program
	print(""" 

 ************ Welcome To Student Management System **************
 

Enter 1 : To View List of Students 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student   """)
	

	try: 
		userInput = int(input("Please Select An Above Option: ")) 
	except ValueError:
		exit("\n That's Not A Number") 
	else:
		print("\n") 

	#Checking Using Option	
	if(userInput == 1): #Print List Of Students
		print("List Students\n")  
		for students in listStd:
			print("=> {}".format(students))

	elif(userInput == 2): #Add New Student In The List
		newStd = input("Enter New Student: ")
		if(newStd in listStd): #Checks The New Student Is Already In List Ur Not
			print("\nThis Student {} Already In The Database".format(newStd))  
		else:	
			listStd.append(newStd)
			print("\n=> New Student {} Successfully Add \n".format(newStd))
			for students in listStd:
				print("=> {}".format(students))	

	elif(userInput == 3): #Search Student From The List
		srcStd = input("Enter Student Name To Search: ")
		if(srcStd in listStd): #This Condition Searching The Student
			print("\n=> Record Found Of Student {}".format(srcStd))
		else:
			print("\n=> No Record Found Of Student {}".format(srcStd)) #Error Message

	elif(userInput == 4): #Remove Student From The List
		rmStd = input("Enter Student Name To Remove: ")
		if(rmStd in listStd): #This Condition Removing The Student From The List 
			listStd.remove(rmStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmStd))
			for students in listStd:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(rmStd)) #Error Message
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")		
						

Student()

def runAgain(): 
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): 
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		Student()
		runAgain()
	else:
		quit(bye) 

runAgain()		
