import customtkinter
import matplotlib
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()

Red_score = 0
Green_score = 0
Yellow_score = 0
Blue_score = 0

#app.geometry(f"{width}x{height}")
#app.attributes('-fullscreen', True)
app.title("Scoreboard")
app.config(bg='#202123')

def show():
    global Red_score   
    Red_x = 1
    Blue_x = 2
    Green_x = 3
    Yellow_x = 4
    plt.bar(Red_x, Red_score,  label = "Red House", color = "Red")
    plt.bar(Blue_x, Blue_score, label = "Blue House", color = "Blue")
    plt.bar(Green_x, Green_score, label = "Green House", color = "Green")
    plt.bar(Yellow_x, Yellow_score, label = "Yellow House", color = "Yellow")
    plt.xlabel("Houses")
    plt.yticks(fontsize = 20)
    plt.title("Score Board", fontsize="40")
    
    plt.show()

def Red_add10_func():
    global Red_score
    Red_score += 10
    plt.clf()
    show()
def Red_sub10_func():
    global Red_score
    Red_score -= 10
    plt.clf()
    show()

def Red_add5_func():
    global Red_score
    Red_score += 5
    plt.clf()
    show()
def Red_sub5_func():
    global Red_score
    Red_score -= 5
    plt.clf()
    show()

#blue

def Blue_add10_func():
    global Blue_score
    Blue_score += 10
    plt.clf()
    show()
def Blue_sub10_func():
    global Blue_score
    Blue_score -= 10
    plt.clf()
    show()
def Blue_add5_func():
    global Blue_score
    Blue_score += 5
    plt.clf()
    show()
def Blue_sub5_func():
    global Blue_score
    Blue_score -= 5
    plt.clf()
    show()
    
def Green_add10_func():
    global Green_score
    Green_score += 10
    plt.clf()
    show()
def Green_sub10_func():
    global Green_score
    Green_score -= 10
    plt.clf()
    show()

def Green_add5_func():
    global Green_score
    Green_score += 5
    plt.clf()
    show()
def Green_sub5_func():
    global Green_score
    Green_score -= 5
    plt.clf()
    show()
    
#Yellow
def Yellow_add10_func():
    global Yellow_score
    Yellow_score += 10
    plt.clf()
    show()
def Yellow_sub10_func():
    global Yellow_score
    Yellow_score -= 10
    plt.clf()
    show()
def Yellow_add5_func():
    global Yellow_score
    Yellow_score += 5
    plt.clf()
    show()
def Yellow_sub5_func():
    global Yellow_score
    Yellow_score -= 5
    plt.clf()
    show()
#BUTTONS
Red_plus_10=customtkinter.CTkButton(
    master = app,
    command = Red_add10_func,
    text = "+10",
    fg_color="Red",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Red_sub_10=customtkinter.CTkButton(
    master = app,
    command = Red_sub10_func,
    text = "-10",
    fg_color="Red",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Red_plus_5=customtkinter.CTkButton(
    master = app,
    command = Red_add5_func,
    text = "+5",
    fg_color="Red",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Red_sub_5=customtkinter.CTkButton(
    master = app,
    command = Red_sub5_func,
    text = "-5",
    fg_color="Red",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

#BLUE
Blue_plus_10=customtkinter.CTkButton(
    master = app,
    command = Blue_add10_func,
    text = "+10",
    fg_color="Blue",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Blue_sub_10=customtkinter.CTkButton(
    master = app,
    command = Blue_sub10_func,
    text = "-10",
    fg_color="Blue",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Blue_plus_5=customtkinter.CTkButton(
    master = app,
    command = Blue_add5_func,
    text = "+5",
    fg_color="Blue",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Blue_sub_5=customtkinter.CTkButton(
    master = app,
    command = Blue_sub5_func,
    text = "-5",
    fg_color="Blue",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

#Green

Green_plus_10=customtkinter.CTkButton(
    master = app,
    command = Green_add10_func,
    text = "+10",
    fg_color="Green",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Green_sub_10=customtkinter.CTkButton(
    master = app,
    command = Green_sub10_func,
    text = "-10",
    fg_color="Green",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Green_plus_5=customtkinter.CTkButton(
    master = app,
    command = Green_add5_func,
    text = "+5",
    fg_color="Green",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Green_sub_5=customtkinter.CTkButton(
    master = app,
    command = Green_sub5_func,
    text = "-5",
    fg_color="Green",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

#Yelllow

Yellow_plus_10=customtkinter.CTkButton(
    master = app,
    command = Yellow_add10_func,
    text = "+10",
    fg_color="Yellow",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Yellow_sub_10=customtkinter.CTkButton(
    master = app,
    command = Yellow_sub10_func,
    text = "-10",
    fg_color="Yellow",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Yellow_plus_5=customtkinter.CTkButton(
    master = app,
    command = Yellow_add5_func,
    text = "+5",
    fg_color="Yellow",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Yellow_sub_5=customtkinter.CTkButton(
    master = app,
    command = Yellow_sub5_func,
    text = "-5",
    fg_color="Yellow",
    text_color="black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

show_plot=customtkinter.CTkButton(
    master = app,
    command = show,
    text = "show bargraph",
    fg_color="White",
    text_color="Black",
    width = 35,
    height = 35,
    corner_radius = 5,
)

Red_plus_10.pack(padx = 10, pady= 10)
Red_sub_10.pack(padx = 10, pady= 10)
Red_plus_5.pack(padx = 10, pady= 10)
Red_sub_5.pack(padx = 10, pady= 10)

Blue_plus_10.pack(padx = 10, pady= 10)
Blue_sub_10.pack(padx = 10, pady= 10)
Blue_plus_5.pack(padx = 10, pady= 10)
Blue_sub_5.pack(padx = 10, pady= 10)

Green_plus_10.pack(padx = 10, pady= 10)
Green_sub_10.pack(padx = 10, pady= 10)
Green_plus_5.pack(padx = 10, pady= 10)
Green_sub_5.pack(padx = 10, pady= 10)

Yellow_plus_10.pack(padx = 10, pady= 10)
Yellow_sub_10.pack(padx = 10, pady= 10)
Yellow_plus_5.pack(padx = 10, pady= 10)
Yellow_sub_5.pack(padx = 10, pady= 10)

show_plot.pack(padx = 10, pady= 10)

app.mainloop()