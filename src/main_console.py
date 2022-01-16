
from fpdf import FPDF
from random import randint
# from os import getcwd
# from tkinter import filedialog, Tk, IntVar, Radiobutton,Button

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
def Generate(q_type,digit,filename):
    type_dict = {'1':'+','2':'-','3':'X'}
    
    pdf = PDF(unit='mm',format='Letter')#pdf objec
    for i in range(10):
        pdf.add_page()
        pdf.draw(q_type=type_dict[q_type],digit=int(digit))
    if not filename.endswith('.pdf'):
        pdf.output("{}.pdf".format(filename),'F')
    else:
        pdf.output(filename,'F')

if __name__ == "__main__":
    print("Welcome to Kuomon Generator!")
    print("Please select question type:")
    print("     1: Addition")
    print("     2: Subtraction")
    print("     3: Multiplication")
    q_type = input("Quation type:")
    print("How many digits? (Up to 5)")
    digit = input("Digit:")
    filename = input("File name?")
    Generate(q_type,digit,filename)


