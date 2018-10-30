from easygui import *
import sys
sum=0
while 1:
     msgbox("Welcome To TechBazaar")

     msg="What would you like to shop"
     title="TechBazaar"
     choices=["Mobile","Laptop","Gaming Console"]
     choice=choicebox(msg,title,choices)

     if choice=="Mobile":
        msg1="Choose Brand"
        title1="Brand Choice"
        choices1=["Apple-65000","OnePlus-35000"]
        choice1=choicebox(msg1,title1,choices1)

        if choice1=="Apple-65000":
            sum=sum+65000
        else:
            sum=sum+35000


     elif choice=="Laptop":
          msg1="Choose Brand"
          title1="Brand Choice"
          choices1=["HP-50000","Dell-60000"]
          choice1=choicebox(msg1,title1,choices1)

          if choice1=="HP-50000":
            sum=sum+50000
          else:
            sum=sum+60000

     else:
         msg1="Choose Brand"
         title1="Brand Choice"
         choices1=["Playstation-30000","Xbox-40000"]
         choice1=choicebox(msg1,title1,choices1)

         if choice1=="Playstation-30000":
            sum=sum+30000
         else:
            sum=sum+40000

     msgbox(sum,"Your bill is:")

     msg="Do you want to continue?"
     title="Confirmation"
     if ccbox(msg,title):
         pass
     else:
         sys.exit(0)
