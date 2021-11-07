# for initialising tkinter
from tkinter import *

root = Tk()
root.title("Fibonacci Sum")
root.geometry("350x500+500+100")

root.resizable(False , False)
# adding components
text_input = Entry(root)
label_series = Label(root)
label_sum = Label(root , fg = "darkblue" , font = "fantasy 12")

def popupmsg(msg):
  popup = Tk()
  popup.geometry("200x100+580+400")
  popup.wm_title("Error")
  label = Label(popup, text=msg , fg = "red")
  label.pack(side="top", fill="x", pady=10 )
  popup.resizable(False,False)
  B1 = Button(popup, text="Okay", command = popup.destroy)
  B1.pack(pady=10)
       
# function
def Fibonacci():
  for character in text_input.get():
    if not character.isdigit():
     popupmsg("You need to enter a digit !")
     popup.mainloop()
    else:
     label_series['text'] = ""
     input_1 = int(text_input.get())
     first_no = 0
     second_no = 1
     sum = 0
     counter = 1
     main_sum = 0
     while counter <= input_1:
         label_series['text'] += str(sum) + " "
         first_no = second_no
         second_no = sum
         sum = second_no+first_no
         counter = counter+1
         main_sum = main_sum + sum
         label_sum['text'] = "Fibonacci Sum : " + str(main_sum)
  first_no = 0
  second_no = 1
  sum = 0
  counter = 1
  main_sum = 0
  
   
# adding button
button = Button(root , text="Show Fibonacci Sum" , command = Fibonacci , fg = "white" , bg="red" , font="fantasy 15")

# making components visible on the root window
text_input.pack(pady=10)
label_series.pack(pady=10)
label_sum.pack(pady=10)
button.pack(pady=10)

root.mainloop()