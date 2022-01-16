
from fpdf import FPDF
from random import randint
from os import getcwd
from tkinter import filedialog, Tk, IntVar, Radiobutton,Button

pdf_w = 210
pdf_h = 250
n_row = 6
n_col = 5
cell_w = pdf_w/n_col
cell_h = pdf_h/n_row
class PDF(FPDF):
     def draw(self,q_type,digit):
            self.set_line_width(0.0)
            for row_idx in range(n_row):
                for col_idx in range(n_col):
                    origin = [cell_w*col_idx, cell_h*row_idx]
                    x1 = origin[0]+cell_w/10
                    x2 = x1+cell_w/5*4
                    y1 = origin[1]+cell_h/5*4
                    y2 = y1
                    self.line(x1,y1,x2,y2 )
                    
                    self.set_xy(origin[0]+cell_w/10,origin[1]+cell_h/5*3)
#                     self.image('division.png',w=cell_h*0.2, h=cell_h*0.2)
                    self.set_font('Arial', 'B', 24)
#                     self.set_text_color(220, 50, 50)
                    a = randint(1,10**digit-1)
                    b = randint(1,10**digit-1)
                    if q_type == '-':
                        a, b = max(a,b), min(a,b)
                    
    
                    txt1 = "{}".format(a)
                    txt2 = "{}  {}".format(q_type,b)
                    self.set_xy(origin[0]+cell_w/2,origin[1]+cell_h/5*2)
                    self.cell(w=cell_h*0.2, h=cell_h*0.2, align='R', txt=txt1,border=0)
                    self.set_xy(origin[0]+cell_w/2,origin[1]+cell_h/5*3)
                    self.cell(w=cell_h*0.2, h=cell_h*0.2, align='R', txt=txt2,border=0)



def Generate(q_type,digit):
    filename = filedialog.asksaveasfilename(initialdir = getcwd(),title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    type_dict = {1:'+',2:'-',3:'X'}
    
    pdf = PDF(unit='mm',format='Letter')#pdf objec
    for i in range(10):
        pdf.add_page()
        pdf.draw(q_type=type_dict[q_type],digit=digit)
    
    pdf.output(filename,'F')

master = Tk()
master.title('Kumon generator')
master.geometry("300x150")
q_type = IntVar()
digit = IntVar()
q_type.set(1)
digit.set(1)
# TypeList=Radiobutton(master)
R1 = Radiobutton(master, text="Addition", variable=q_type, value=1)
R1.grid(row=0,column=0, sticky = 'w' )

R2 = Radiobutton(master, text="Subtraction", variable=q_type, value=2)
R2.grid(row=1,column=0,sticky = 'w' )

R3 = Radiobutton(master, text="Multiplication", variable=q_type, value=3)
R3.grid(row=2,column=0,sticky = 'w')

R4 = Radiobutton(master, text="1 digit", variable=digit, value=1)
R4.grid(row=0,column=1,sticky = 'w')

R5 = Radiobutton(master, text="2 digit", variable=digit, value=2)
R5.grid(row=1,column=1,sticky = 'w')

R6 = Radiobutton(master, text="3 digit", variable=digit, value=3)
R6.grid(row=2,column=1,sticky = 'w')

R7 = Radiobutton(master, text="4 digit", variable=digit, value=4)
R7.grid(row=3,column=1,sticky = 'w')

R8 = Radiobutton(master, text="5 digit", variable=digit, value=5)
R8.grid(row=4,column=1,sticky = 'w')




B = Button(master, text="Generate",command=lambda :Generate(q_type.get(),digit.get()) )
B.grid(row=6,column=0,sticky='w')
# B.pack()
master.mainloop()