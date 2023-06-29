from tkinter import *
from tkinter import OptionMenu
from tkinter.messagebox import *
import tkinter.font as tkFont
from mpmath import *
from sympy import integrate, symbols, sympify, Basic

class guiForIntegrals():
    def __init__(self, root):
        #setting title
        root.title("Integrals")
        options = [
            "Single",
            "Double",
            "Triple"
        ]
        def CartesianIntegrals(choice,equationInput):
            func=sympify(equationInput,evaluate=True)
            a,b,x=symbols("a b x")
            equation1=integrate(func,(x,a,b))
            equation1a=integrate(func,(x,a,b))
            equation2=equation1.evalf(subs={ a: self.EntryBoxVarA.get("1.0", "1.0 lineend"),b: self.EntryBoxVarB.get("1.0", "1.0 lineend")})
            if (choice=='2' or choice =='3'):
                y,c,d=symbols("y c d")
                equation3=integrate(equation2,(y,c,d))
                equation3a=integrate(equation2,(y,c,d))
                equation4=equation3.evalf(subs={c: self.EntryBoxVarC.get("1.0", "1.0 lineend"),d: self.EntryBoxVarD.get("1.0", "1.0 lineend")})
                if (choice=='3'):
                    z,e,f=symbols("z e f")
                    equation5=integrate(equation4,(z,e,f))
                    equation5a=integrate(equation4,(z,e,f))
                    equation6=equation5.evalf(subs={e: self.EntryBoxVarE.get("1.0", "1.0 lineend"),f: self.EntryBoxVarF.get("1.0", "1.0 lineend")})
                    return equation6
                else:
                    return equation4
            else:
                return equation2
        def Config(equationInput):    
            typeOfCordsSystems='1'
            if (typeOfCordsSystems=='1'):
                if (clicked.get()=="Single"):
                    return CartesianIntegrals('1', equationInput)
                elif (clicked.get()=="Double"):
                    return CartesianIntegrals('2', equationInput)
                elif (clicked.get()=="Triple"):
                    return CartesianIntegrals('3', equationInput)
                    
                else:
                    
                    print("Error: Integral type does not exist.")
            else:
                print("Error: System of that ID does not exist.")
                
        #setting window size
        width=450
        height=222
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.output=""
        self.entry = Text(width=29,height=1)
        self.entry.place(x=80,y=10)

        self.GLabel_415=Label(root)
        self.GLabel_415["text"] = "Function:"
        self.GLabel_415.place(x=10,y=10,width=70,height=25)

        self.GLabel_152=Label(root)
        self.GLabel_152["text"] = "X:"
        self.GLabel_152.place(x=10,y=40,width=70,height=25)

        self.EntryBoxVarA=Text(root)
        self.EntryBoxVarA.place(x=110,y=40,width=70,height=25)

        self.GLabel_753=Label(root)
        self.GLabel_753["text"] = "A:"
        self.GLabel_753.place(x=80,y=40,width=30,height=30)
        
        self.GLabel_111=Label(root)        
        self.GLabel_111["text"] = "B:"
        self.GLabel_111.place(x=180,y=40,width=37,height=30)

        self.EntryBoxVarB=Text(root)
        self.EntryBoxVarB.place(x=210,y=40,width=70,height=25)

        self.EntryBoxVarC=Text(root)
        self.EntryBoxVarC.place(x=110,y=80,width=70,height=25)

        self.GLabel_210=Label(root)
        self.GLabel_210["text"] = "C:"
        self.GLabel_210.place(x=80,y=80,width=30,height=30)

        self.GLabel_431=Label(root)
        self.GLabel_431["text"] = "D:"
        self.GLabel_431.place(x=180,y=80,width=30,height=30)

        self.GLabel_252=Label(root)        
        self.GLabel_252["text"] = "Y:"
        self.GLabel_252.place(x=10,y=80,width=70,height=25)

        self.GLabel_715=Label(root)
        self.GLabel_715["text"] = "Z:"
        self.GLabel_715.place(x=10,y=120,width=70,height=25)

        self.GLabel_798=Label(root)
        self.GLabel_798["text"] = "E:"
        self.GLabel_798.place(x=60,y=120,width=70,height=25)

        self.GLabel_483=Label(root)
        self.GLabel_483["text"] = "F:"
        self.GLabel_483.place(x=160,y=120,width=70,height=25)

        self.EntryBoxVarE=Text(root)
        self.EntryBoxVarE.place(x=110,y=120,width=70,height=25)

        self.EntryBoxVarF=Text(root)
        self.EntryBoxVarF.place(x=210,y=120,width=70,height=25)

        self.OutputText=Text(root)
        self.OutputText.place(x=130,y=170,width=217,height=25)

        self.EntryBoxVarD=Text(root)
        self.EntryBoxVarD.place(x=210,y=80,width=70,height=25)
        def getString():
            string1=self.entry.get("1.0", "1.0 lineend")
            self.output=Config(string1)
            self.OutputText.delete("1.0","end")
            self.OutputText.insert(END,(self.output))
        
        clicked = StringVar()
        clicked.set( "Single" )
        self.button = Button(text="Calculate",command=getString)
        self.button.place(x=360,y=10,width=70,height=25)
        self.dropdown = OptionMenu(root, clicked, *options)
        self.dropdown.place(x=360,y=50,width=70,height=25)
        OutputLabel=Label(root)
        OutputLabel["text"] = "Output:"
        OutputLabel.place(x=50,y=170,width=70,height=25)
if __name__=='__main__':
    myTkRoot = Tk()
    app = guiForIntegrals(myTkRoot)
    myTkRoot.mainloop()
