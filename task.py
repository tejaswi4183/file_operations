#!/usr/bin/python3
import shutil
import os
a=1;
def copy():
	print("If u want to copy a \n 1. Directory \n 2.File\n")
	fi=int(input())
	if(fi==1):
		print("Enter Directory name:")
		directory=input()
		print("current path=",os.getcwd())
		print("\nselect one To check if directory  exists or not\n 1.Relative path \n 2.Absolute path\n")
		z=int(input())
		if(z==1):
			path=directory
			c=os.path.exists(path)
			if (c):
				print("\n\nDirectory exits\n\n")
				print("enter another Directory name to copying")
				directory2=input()
				
				print("if you want to copy a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					copying=shutil.copytree(directory,directory2)
					if(copying==directory2):
						print("\n***Copying Successfully***\n")
					else:
						print("\n***Unsuccesfull***\n")
				elif(p==2):
					print("Current path =",os.getcwd())
					print("Enter path include directory name")
					path=input()
					copying=shutil.copytree(directory,path)
					if(copying==path):
						print("\n***Copying Successfully***\n")
					else:
						print("\n***Unsuccesfull***\n")	
				else:
					print("enter Correct option")
			else:
				print("Directory doesn't exists")
				print("enter correct path")
		elif(z==2):
			path=input("Enter path:")
			c=os.path.exists(path)
			if (c):
				print("\n\nDirectory exits\n\n")
				print("enter another Directory name to copying")
				directory2=input()
				
				print("if you want to copy a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					copying=shutil.copytree(directory,directory2)
					if(copying==directory):
						print("\n***Copying Successfully***\n")
					else:
						print("\n***Copying Unsuccesfully***\n")
				elif(p==2):
					print("Current path=",os.getcwd())
					print("Enter path include directory name")
					path=input()
					copying=shutil.copytree(directory,path)
					if(copying==path):
						print("\n***Copying Successfull***\n")
					else:
						print("\n***Unsuccesfull***\n")	
				else:
					print("enter Correct option")
			else:
				print("Directory doesn't exits")
				print("enter correct path")
		else:
			print("Enter correct option")
			
					
	elif(fi==2):
		print("Enter file name")
		filename=input()
		print("current path=",os.getcwd())
		print("\nselect one to check if file exits or not \n 1.Relative path \n 2.Absolute path\n")
		z=int(input())
		if(z==1):
			path=filename
		
			c=os.path.exists(path)
			
			if (c):
				print("\n\nfile exits\n\n")
				print("enter another file name to copying")
				file2=input()
				print("if you want to copy a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					copying=shutil.copy(filename,file2)
					if(copying==file2):
						print("\n\n***Copying Successfully***\n\n")
					else:
						print("\n***unsuccessfull***\n")
				elif(p==2):
					print("current path=",os.getcwd())
					print("enter path ")
					path=input()
					copying=shutil.copytree(filename,path)
					if(copying==path):
						print("\n\n***Copying Successfully***\n\n")
					else:
						print("\n***Unsuccessfull***\n")

				else:
					print("enter correct option")
						
			else:
				print("file doesn't exits")
				print("Enter correct path")
		elif(z==2):
						
			path=input("Enter path:")
				
			c=os.path.exists(path)
				
			if (c):
				print("\n\nfile exits\n\n")
				print("enter another file name to copying")
				file2=input()
				print("if you want to copy a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					copying=shutil.copy(filename,file2)
					if(copying==file2):
						print("\n\n***Copying Successfully***\n\n") 
					else:
						print("***unsuccessfull***")
				elif(p==2):
					print("current path=",os.getcwd())
					print("enter path ")
					path=input()
					copying=shutil.copy(filename,path)
					print("\n\n***Copying Successfully***\n\n")
		
				else:
					print("enter correct option")
			else:
				print("file doesn't exits")
				print("Enter correct path")
		else:
			print("enter correct option")
	else:
		print("enter corrct option")
def move():
	print("If u want to Move a \n 1. Directory \n 2.File\n")
	fi=int(input())
	if(fi==1):
		print("Enter Directory name:")
		directory=input()
		print("current path=",os.getcwd())
		print("\nselect one To check if directory  exists or not\n 1.Relative path \n 2.Absolute path\n")
		z=int(input())
		if(z==1):
			path=directory
			c=os.path.exists(path)
			if (c):
				print("\n\nDirectory exits\n\n")
				print("enter another Directory name to Moving")
				directory2=input()
				
				print("if you want to move a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					moving=shutil.move(directory,directory2)
					if(moving==directory2):
						print("\n***Moving Successfully***\n")
					else:
						print("\n***Unsuccesfull***\n")
				elif(p==2):
					print("Enter path include directory name")
					path=input()
					moving=shutil.move(directory,path)
					if(moving==path):
						print("\n***Moving Successfully***\n")
					else:
						print("\n***Unsuccesfull***\n")	
				else:
					print("enter Correct option")
			else:
				print("Directory doesn't exists")
				print("enter correct path")
		elif(z==2):
			path=input("Enter path:")
			c=os.path.exists(path)
			if (c):
				print("\n\nDirectory exits\n\n")
				print("enter another Directory name to moving")
				directory2=input()
				
				print("if you want to move a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					moving=shutil.move(directory,directory2)
					if(moving==directory):
						print("\n***Moving Successfully***\n")
					else:
						print("\n***Moving Unsuccesfully***\n")
				elif(p==2):
					print("Enter path include directory name")
					path=input()
					moving=shutil.move(directory,path)
					if(moving==path):
						print("\n***Moving Successfull***\n")
					else:
						print("\n***Unsuccesfull***\n")	
				else:
					print("enter Correct option")
			else:
				print("Directory doesn't exits")
				print("enter correct path")
		else:
			print("Enter correct option")
			
					
	elif(fi==2):
		print("Enter file name")
		filename=input()
		print("current path=",os.getcwd())
		print("\nselect one to check if file exits or not \n 1.Relative path \n 2.Absolute path\n")
		z=int(input())
		if(z==1):
			path=filename
		
			c=os.path.exists(path)
			
			if (c):
				print("\n\nfile exits\n\n")
				print("enter another file name to moving")
				file2=input()
				print("if you want to move a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					moving=shutil.move(filename,file2)
					if(moving==file2):
						print("\n\n***moving Successfully***\n\n")
					else:
						print("\n***unsuccessfull***\n")
				elif(p==2):
					print("current path=",os.getcwd())
					print("enter path ")
					path=input()
					moving=shutil.move(filename,path)
					if(moving==path):
						print("\n***Moving Successfully***\n")
					else:
						print("\n***Unsuccessfull***\n")

				else:
					print("enter correct option")
						
			else:
				print("file doesn't exits")
				print("Enter correct path")
		elif(z==2):
						
			path=input("Enter path:")
				
			c=os.path.exists(path)
				
			if (c):
				print("\n\nfile exits\n\n")
				print("enter another file name to moving")
				file2=input()
				print("if you want to move a file in \n 1.same path \n 2.another path \n")
				p=int(input())
				if(p==1):
					moving=shutil.move(filename,file2)
					if(moving==file2):
						print("\n***Moving Successfully***\n")
					else:
						print("\n***unsuccessfull***\n")
				elif(p==2):
					print("current path=",os.getcwd())
					print("enter path ")
					path=input()
					
					
					moving=shutil.move(filename,path)
					
					print("\n\n***Copying Successfully***\n\n")
		
				else:
					print("enter correct option")
			else:
				print("file doesn't exits")
				print("Enter correct path")
		else:
			print("enter correct option")
	else:
		print("enter correct option")
def rename():
	print("If you want to rename \n 1.a directory \n 2.a file\n")
	z=int(input())
	if(z==1):
		print("enter directory name")
		directory=input()
		print("select one to check directory exists or not\n 1.Relative path \n 2. Absolute path\n")
		p=int(input())
		if(p==1):
			path=directory
			c=os.path.exists(path)
			if(c):
				print("\nDirectory Exists\n")
				print("Change Directory name:")
				rename=input()
				d=shutil.move(directory,rename)
				if(d==rename):
					print("\n\n***Renaming Succesfully***\n\n")
				else:
					print("\n\n ***Unsuccessfull***\n")
			else:
				print("Directory doesn't exists")
				print("enter correct path")
		elif(p==2):
			print("Current path =",os.getcwd())
			print("Enter path")
			path=input()
			c=os.path.exists(path)
			if(c):
				print("\nDirectory Exists\n")
				print("Change Directory name:")
				rename=input()
				d=shutil.move(directory,rename)
				if(d==rename):
					print("\n\n***Renaming Succesfully***\n\n")
				else:
					print("\n\n ***Unsuccessfull***\n")
			else:
				print("Directory doesn't exists")
				print("enter correct path")
		else:
			print("Enter correct option")
	elif(z==2):
		print("enter File name")
		filename=input()
		print("select one to check File exists or not\n 1.Relative path \n 2. Absolute path\n")
		p=int(input())
		if(p==1):
			path=filename
			c=os.path.exists(path)
			if(c):
				print("\nFile Exists\n")
				print("Change File name:")
				rename=input()
				d=shutil.move(filename,rename)
				if(d==rename):
					print("\n\n***Renaming Succesfully***\n\n")
				else:
					print("\n\n ***Unsuccessfull***\n")
			else:
				print("Directory doesn't exists")
				print("enter correct path")
		elif(p==2):
			print("Current path =",os.getcwd())
			print("Enter path")
			path=input()
			c=os.path.exists(path)
			if(c):
				print("\n	File Exists\n")
				print("Change File name:")
				rename=input()
				d=shutil.move(filename,rename)
				if(d==rename):
					print("\n\n***Renaming Succesfully***\n\n")
				else:
					print("\n\n ***Unsuccessfull***\n")
			else:
				print("Directory doesn't exists")
				print("enter correct path")
		else:
			print("Enter correct option")
	else:
		print("enter correct one")
def delete():
	print("Deletion Type \n 1.Permanent Deletion \n 2.Move to Trash")
	z=int(input())
	if(z==1):
		print("Select one to delete \n 1.Directory \n 2.File")
		delete=int(input())
		if(delete==1):
			p=input("Enter Directory name to delete:")
			print("enter path to check if directory exists or not \n 1.Relative path \n 2.Absolute path")
			directory=int(input())
			if(directory==1):
				path=p
				c=os.path.exists(path)
				if(c):
					print("**Directory exists**")
					shutil.rmtree(path)
					print("\n\n***Deletion Successfully***\n\n")
				else:
					print("*Directory Doesn't exists \n enter correct path")
			elif(directory==2):
				print("Current path =",os.getcwd())
				path=input("enter path:")
				c=os.path.exists(path)
				if(c):
					print("**Directory exists**")
					shutil.rmtree(path)
					print("\n\n***Deletion Successfully***\n\n")
				else:
					print("*Directory Doesn't exists \n enter correct path")
			else:
				print("Enter Correct option")
		elif(delete==2):
			p=input("Enter File name to delete:")
			print("enter path to check if File exists or not \n 1.Relative path \n 2.Absolute path")
			filename=int(input())
			if(filename==1):
				path=p
				c=os.path.exists(path)
				if(c):
					print("**File exists**")
					shutil.unlink(path)
					print("\n\n***Deletion Successfully***\n\n")
				else:
					print("*File Doesn't exists \n enter correct path")
			elif(filename==2):
				print("Current path =",os.getcwd())
				path=input("enter path:")
				c=os.path.exists(path)
				if(c):
					print("**File exists**")
					shutil.unlink(path)
					print("\n\n***Deletion Successfully***\n\n")
				else:
					print("File Doesn't exists \n enter correct path")
			else:
				print("Enter Correct option")
		else:
			print("** enter correct path")
	elif(z==2):
		print("Select one to Remove \n 1.Directory \n 2.File")
		delete=int(input())
		if(delete==1):
			print("Enter Directory name to Remove:")
			p=input()
			print("enter path to check if directory exists or not \n 1.Relative path \n 2.Absolute path")
			directory=int(input())
			if(directory==1):
				path=p
				c=os.path.exists(path)
				if(c):
					print("**Directory exists**")
					Trash=".local/share/Trash/"
					shutil.move(path,Trash)
					print("\n\n***Removing Successfully***\n\n")
				else:
					print("*Directory Doesn't exists \n enter correct path")
			elif(directory==2):
				print("Current path =",os.getcwd())
				path=input("enter path:")
				c=os.path.exists(path)
				if(c):
					print("**Directory exists**")
					Trash=".local/share/Trash/"
					shutil.move(path,Trash)
					print("\n\n***Removing Successfully***\n\n")
				else:
					print("*Directory Doesn't exists \n enter correct path")
			else:
				print("Enter Correct option")
		elif(delete==2):
			print("Enter File name to remove:")
			p=input()
			print("enter path to check if File exists or not \n 1.Relative path \n 2.Absolute path")
			filename=int(input())
			if(filename==1):
				path=p
				c=os.path.exists(path)
				if(c):
					print("**File exists**")
					Trash=".local/share/Trash/"
					shutil.move(path,Trash)
					print("\n\n***Removing Successfully***\n\n")
				else:
					print("*File Doesn't exists \n enter correct path")
			elif(filename==2):
				print("Current path =",os.getcwd())
				path=input("enter path:")
				c=os.path.exists(path)
				if(c):
					print("**File exists**")
					Trash=".local/share/Trash/"
					shutil.move(path,Trash)
					print("\n\n***Removing Successfully***\n\n")
				else:
					print("File Doesn't exists \n enter correct path")
			else:
				print("Enter Correct option")
		else:
			print("**enter correct path")
	else:
		print("Enter Correct Option")
	
		
while(a):
	print("\n\n\t***Menu Driven Program***\n")
	print("  1.Copy \n  2.Move \n  3.Rename \n  4.Deletion \n  5.exit\n")
	choice=int(input("Enter a choice :"))
	if(choice==1):
		copy()
	elif(choice==2):
		move()
	elif(choice==3):
		rename()
	elif(choice==4):
		delete()
	elif(choice==5):
		exit()
	else:
		print("enter correct number")
	
		
