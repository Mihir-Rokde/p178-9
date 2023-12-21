from tkinter import*
import random
root=Tk()
root.title("Encapsulation")
root.geometry("500x400")
root.configure(background="white")
ls=Label(root,text="Score : 0",bg="white",font=("Times",15,"bold"))
ls.place(relx=0.1,rely=0.1,anchor=CENTER)
ln=Label(root,bg="white",font=("Arial",15,"bold"))
ln.place(relx=0.5,rely=0.3,anchor=CENTER)
iv=Entry(root)
iv.place(relx=0.5,rely=0.5,anchor=CENTER)
class game:
    def __init__(self):
         self.__score=0
    def updategame(self):
         self.text=["RED","BLUE","YELLOW","GREEN","PURPLE","BLACK","ORANGE"]
         self.rnt=random.randint(0,6)
         self.color=["red","blue","yellow","green","pruple","black","orange"]
         self.rnc=random.randint(0,6)
         ln["text"]=self.text[self.rnt]
         ln["fg"]=self.color[self.rnc]
    def __updatescore(self,iv):
         if(iv==self.color[self.rnc]):
              print(self.color[self.rnc])
              self.__score=self.__score+random.randint(0,10)
              ls["text"]="score : "+str(self.__score)
    def getuservalue(self,iv):
         self.__updatescore(iv)
obj=game()
def getinput():
     value=iv.get()
     obj.getuservalue(value)
     obj.updategame()
     iv.delete(0,END)
button=Button(root,text="Check",command=getinput)
button.place(relx=0.35,rely=0.65,anchor=CENTER)
button1=Button(root,text="Start",command=obj.updategame)
button1.place(relx=0.65,rely=0.65,anchor=CENTER)

root.mainloop()