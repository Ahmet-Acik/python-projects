# # python calculator

options = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if options == "+":
    print(round(num1 + num2, 1))
elif options == "-":
    print(round(num1 - num2, 1))
elif options == "*":
    print(round(num1 * num2), 1)
elif options == "/":
    if num1 == 0 or num2 == 0:
        print("Cannot divide by zero")
    else:
        print(round(num1 / num2, 1))
else:
    print("Invalid operator")


# # Importing the tkinter module
# from tkinter import *

# # Creating a window
# root = Tk()

# # Setting the title of the window
# root.title("Calculator")

# # Setting the geometry of the window
# root.geometry("400x600")

# # Setting the maximum size of the window
# root.maxsize(400, 600)

# # Setting the minimum size of the window
# root.minsize(400, 600)

# # Creating a function to add the value to the input field


# def click(event):
#     global scvalue
#     text = event.widget.cget("text")
#     if text == "=":
#         if scvalue.get().isdigit():
#             value = int(scvalue.get())
#         else:
#             try:
#                 value = eval(screen.get())
#             except Exception as e:
#                 value = "Error"
#         scvalue.set(value)
#         screen.update()
#     elif text == "C":
#         scvalue.set("")
#         screen.update()
#     else:
#         scvalue.set(scvalue.get() + text)
#         screen.update()

# # Creating a StringVar object to store the value of the input field
# scvalue = StringVar()
# scvalue.set("")
# screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
# screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# # Creating a frame for the buttons
# f = Frame(root, bg="grey")

# # Creating the buttons
# b = Button(f, text="9", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="8", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="7", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="+", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# f.pack()

# f = Frame(root, bg="grey")

# b = Button(f, text="6", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="5", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="4", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="-", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# f.pack()

# f = Frame(root, bg="grey")

# b = Button(f, text="3", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="2", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="1", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)


# b = Button(f, text="*", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# f.pack()

# f = Frame(root, bg="grey")

# b = Button(f, text="C", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="0", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="=", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# b = Button(f, text="/", font="lucida 20 bold")
# b.pack(side=LEFT, padx=10, pady=10)
# b.bind("<Button-1>", click)

# f.pack()

# # Running the mainloop
# root.mainloop()

# # End of the code

# # Output:
