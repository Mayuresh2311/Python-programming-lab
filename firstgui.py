from easygui import *
import sys
while 1:
    msgbox("Hello people!")

    msg ="What is your favorite subject?"
    title = "subject Survey"
    choices = ["calculus", "python", "electrical engineering", "applied science"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Nevermind you are going to fail in this subject , haha , lol!"
    title = "i feel sorry for you"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
sys.exit(0)
