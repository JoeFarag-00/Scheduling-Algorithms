import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk()
app.geometry("500x780")
app.title("Scheduling Algorithms")

def button_callback():
    Inputs = Entry_Values.get()
    Filt_Vals = Inputs.split(",")  
    Input_List = []
    for value in Filt_Vals:
        Input_List.append(int(value)) 
    print(Input_List, choice)

def slider_callback(value):
    progressbar_1.set(value)
    
def Algo_Option_Callback(c):
    global choice
    choice = c
    if choice == "Optimal":
        Main_Label.configure(text="Page Replacement")
    elif choice == "Second Chance":
        Main_Label.configure(text="Page Replacement")
    elif choice == "C-Scan":
        Main_Label.configure(text="Disk Scheduling")
    elif choice == "Look":
        Main_Label.configure(text="Disk Scheduling")

Main_Frame = customtkinter.CTkFrame(master=app)
Main_Frame.pack(pady=20, padx=60, fill="both", expand=True)

Main_Label = customtkinter.CTkLabel(master=Main_Frame, justify=customtkinter.LEFT,text="Algorithms",font=("System", 30, "bold"))
Main_Label.pack(pady=10, padx=10)

Algo_Option = customtkinter.CTkOptionMenu(Main_Frame, values=["Optimal", "Second Chance", "C-Scan", "Look"],command=Algo_Option_Callback)
Algo_Option.pack(pady=10, padx=10)
Algo_Option.set("Choose Algorithm")

Entry_Values = customtkinter.CTkEntry(master=Main_Frame, placeholder_text="Enter Values...", width=300)
Entry_Values.pack(pady=10, padx=10)

Load_Btn = customtkinter.CTkButton(master=Main_Frame, command=button_callback, text="Run")
Load_Btn.pack(pady=10, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=Main_Frame)
progressbar_1.pack(pady=10, padx=10)

slider_1 = customtkinter.CTkSlider(master=Main_Frame, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)



text_1 = customtkinter.CTkTextbox(master=Main_Frame, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

app.mainloop()