"""
Reverse Polish Notation Calculator
"""

from main import Stack, TransformExpression, Solution
from tkinter import *

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("RPN CALCULATOR")

if __name__ == '__main__':
    EXPRESSION = ""
    stack_test = Stack()
    RPN = TransformExpression(stack_test)


def btn_click(item):
    global EXPRESSION
    EXPRESSION = EXPRESSION + str(item)
    unexpected_combos = ['+-', '+*', '+/', '+^', '-+', '-*', '-/', '-^', '*+', '*-',
                         '*/', '*^', '/+', '/-', '/*', '/^', '^+', '^-', '^*', '^/',
                         '++', '--', '**', '//', '^^', '+.', '-.', '*.', '/.', '^.',
                         '.+', '.-', '.*', './', '.^']
    if EXPRESSION[-2:] in unexpected_combos:
        EXPRESSION = EXPRESSION[:-1]
    input_text.set(EXPRESSION)


def bt_clear():
    global EXPRESSION
    EXPRESSION = ""
    input_text.set("")


def bt_equal():
    global EXPRESSION
    rpn_list = RPN.to_list(EXPRESSION)
    num1 = Solution(RPN.transformation(rpn_list))
    result = num1.display_calculation(RPN.transformation(rpn_list))
    result_str = str(result)
    if result_str[-2:] == '01':
        result_str = re.sub('[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?01', '', result_str)
        result = float(result_str)
    input_text.set(result)
    EXPRESSION = result_str


input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", 
                    highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", 
                    bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

clear = Button(btns_frame,text="C",fg="black", width=10, height=3, bd=0, bg="#eee", 
               cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, padx=1, pady=1)
left_bracket = Button(btns_frame,text="(",fg="black", width=10, height=3, bd=0, bg="#eee", 
                      cursor="hand2", command=lambda: btn_click('(')).grid(row=0, column=1, padx=1, pady=1)
right_bracket = Button(btns_frame,text=")",fg="black", width=10, height=3, bd=0, bg="#eee", 
                       cursor="hand2", command=lambda: btn_click(')')).grid(row=0, column=2, padx=1, pady=1)
divide = Button(btns_frame,text="/",fg="black", width=10, height=3, bd=0, bg="#eee", 
                cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
seven = Button(btns_frame,text="7",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame,text="8",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame,text="9",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame,text="*",fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
four = Button(btns_frame,text="4",fg="black",width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame,text="5",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame,text="6",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame,text="-",fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
one = Button(btns_frame,text="1",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame,text="2",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame,text="3",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame,text="+",fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
zero = Button(btns_frame,text="0",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, padx=1, pady=1)
exponentiation = Button(btns_frame,text="x^y",fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                        command=lambda: btn_click("^")).grid(row=4, column=1, padx=1, pady=1)
point = Button(btns_frame,text=".",fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame,text="=",fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
