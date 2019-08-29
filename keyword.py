# Coded developed by Varun Pandithurai 
# Date : 29-08-2019
import keyword
keyword.kwlist
name = input("enter the word ")
count=0
for i in keyword.kwlist:
	if i==name :
		print("Is a Keyword")
		count=+1
		break

if count==0 :
	print("Is not a keyword")
			

    
