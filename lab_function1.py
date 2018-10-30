def ArmN(x): #function declaration
 sum=0
 t=x
 while(t>0): #condition statement
  d=t%10     #extracts last digit
  sum+=d**3  #adds the cube
  t=t//10    #removes remaining digits
 if sum==x:  #checks the conditions 
  return 'Armstrong number'
 else:
  return 'not armstrong'
x=int(input()) #input statement
print(ArmN(x)) #print statement

	

		








