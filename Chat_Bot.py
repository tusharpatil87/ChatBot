import tkinter

from Conversation import conv  # for sample training set
from chatterbot import ChatBot  # for chatterbot library
from chatterbot.trainers import ListTrainer  # help to train the model
from tkinter import *

import time  # imported to get solution for clock related error
time.clock = time.time

'''Created object for ChatBot'''
chatbot = ChatBot("Tush Bot")

'''Get assigned imported Sample conversation'''
conversation = conv

'''Train the bot'''
mytrainer = ListTrainer(chatbot)
mytrainer.train(conversation)

try:
    bottk = tkinter.Tk()

    bottk.geometry("450x600")
    bottk.title("My Jarvis Bot")
    pic =PhotoImage(file=r"E:\DS_Projects\Kaggle Datasets\Chat_Boat\venv\img_bot.png")
    new_pic = Label(bottk,image=pic)

    new_pic.pack(pady=6)

    def mybot_try():
        question=bottxt.get()
        response = chatbot.get_response(question)
        botmsg.insert(END, "User : "+question)
        botmsg.insert(END, "ChatBot : " + str(response))
        bottxt.delete(0,END)


    botframe = Frame(bottk)
    botscrl = Scrollbar(botframe)
    botmsg = Listbox(botframe,width=100, height=15)

    botscrl.pack(side=RIGHT,fill=Y)
    botmsg.pack(side=LEFT,fill=BOTH, pady=10)

    botframe.pack()

    bottxt = Entry(bottk, font=('Verdana',20))

    bottxt.pack(fill=X,padx=10, pady=10)

    botbtn = Button(bottk,text="Ask me",font=("Verdana",20), command= mybot_try)
    botbtn.pack()

    bottk.mainloop()


except Exception as e:
    print(e)

