from tkinter import  *
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title("GAME --> Rock, Paper, Scissor")
root.configure(background="white")

# picture
rock_img = ImageTk.PhotoImage(Image.open("C:\\Users\\US\\Desktop\\Python Programming\\files\\stone.JPG"))
paper_img = ImageTk.PhotoImage(Image.open("C:\\Users\\US\\Desktop\\Python Programming\\files\\paper.JPG"))
scissor_img = ImageTk.PhotoImage(Image.open("C:\\Users\\US\\Desktop\\Python Programming\\files\\scissor.JPG"))
rock_img_comp = ImageTk.PhotoImage(Image.open("C:\\Users\\US\\Desktop\\Python Programming\\files\\stone.JPG"))
paper_img_comp  = ImageTk.PhotoImage(Image.open("C:\\Users\\US\\Desktop\\Python Programming\\files\\paper.JPG"))
scissor_img_comp  = ImageTk.PhotoImage(Image.open("C:\\Users\\US\\Desktop\\Python Programming\\files\\scissor.JPG"))

# insert picture
user_label = Label(root, image = scissor_img, bg = "white")
comp_label = Label(root, image = scissor_img_comp, bg = 'white')
user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)


#scores
playerScore = Label(root,text=0,font=100, bg ="white" , fg = "black"  )
computerScore = Label(root,text=0,font=100, bg ="white" , fg = "black")
playerScore.grid(row =1, column =1)
computerScore.grid(row =1, column =3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg ="white" , fg = "black" )
comp_indicator = Label(root,font=50,text="COMPUTER",bg ="white" , fg = "black" )

user_indicator.grid(row=0,column=1)
comp_indicator.grid(row=0,column=3)

#message
msg = Label(root, font=50,bg ="white" , fg = "black")
msg.grid(row = 3,column = 2)


#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore['text'])
    score +=1
    playerScore['text'] = str(score)

#update computer score
def updateCompScore():
    score = int(computerScore['text'])
    score +=1
    computerScore['text'] = str(score)


#check winner
def checking(player,computer):
    if player == computer:
        updateMessage("Its a tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("you loose")
            updateCompScore()
        else:
            updateMessage("you win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("you loose")
            updateCompScore()
        else:
            updateMessage("you win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("you loose")
            updateCompScore()
        else:
            updateMessage("you win")
            updateUserScore()
    else:
        pass

#update choices

choices = ["rock","paper","scissor"]
def updateChoice(x):

    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice =='paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    #for user
    if x=='rock':
        user_label.configure(image=rock_img)
    elif x=='paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checking(x,compChoice)

#buttons
rock = Button(root,width=20, height=2, text="ROCK", bg = "#FF3E4D",command = lambda:updateChoice('rock')).grid(row=2,column=1)
paper = Button(root,width=20, height=2, text="PAPER", bg = "#FAD02E",command = lambda:updateChoice('paper')).grid(row=2,column=2)
scissor = Button(root,width=20, height=2, text="SCISSOR", bg = "#0ABDE3",command = lambda:updateChoice('scissor')).grid(row=2,column=3)

root.mainloop()