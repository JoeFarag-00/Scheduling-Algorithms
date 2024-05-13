import customtkinter
from CTkTable import *
import tkinter
import sys
import os
import turtle
sys.path.append('Algorithms')
from Optimal import Optimal_Page_Replacement
from CScan import CScan
from Second_Chance import second_chance
from Look import Look
# from Look import Looker
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk()
app.geometry("700x720")
app.title("Scheduling Algorithms")

class MainGUI:
    def __init__(self):
        self.app = app
        # Drawer = turtle.RawTurtle(self.canvas)

    def DestroyAll(self):
        widgets = app.winfo_children()
        for widget in widgets:
            widget.destroy()

    def Run_Algo(self):
        if self.Entry_Values.get():
            Inputs = self.Entry_Values.get()
            try:
                Frame = int(self.Entry_Size.get())
            except:
                pass
            Filt_Vals = Inputs.split(",")  
            Input_List = []
            for value in Filt_Vals:
                Input_List.append(int(value)) 
            print(Input_List, choice)
            
            if choice == "Optimal":
                run_optimal = Optimal_Page_Replacement()
                optimal_return, OFault = run_optimal.Optimal_Page_Replacement(Input_List,Frame)
                print(optimal_return, OFault)
                self.Make_Table(optimal_return)
                
            elif choice == "Second Chance":
                run_second = second_chance()
                second_return, SFaults = run_second.second(Frame,Input_List)
                print(second_return, SFaults)
                self.Make_Table(second_return)
            
            elif choice == "C-Scan":
                if self.Path_Choice.get() and self.Initial_Position.get() and self.End_line.get():
                    EndTrack = int(self.End_line.get())
                    Initial = int(self.Initial_Position.get())
                    
                    if self.Path_Choice.get() == "Right":
                        path = True
                    else:
                        path =False

                    run_cscan = CScan(EndTrack, initial_position=Initial, initial_Forward_move=path)
                    run_cscan.add_request(Input_List)
                    cscan_return, SeekTime = run_cscan.schedule()
                    print(cscan_return, SeekTime)
                    
                    self.Draw_Disk(cscan_return, EndTrack)
                    
                    self.Result_Label.configure(text=f"Seek Time: {SeekTime}", fg_color="red")

                else:
                    print("Check Input")
                    
            elif choice == "Look":
                if self.Path_Choice.get() and self.Initial_Position.get() and self.End_line.get():
                    EndTrack = int(self.End_line.get())
                    Initial = int(self.Initial_Position.get())
                    
                    if self.Path_Choice.get() == "Right":
                        path = True
                    else:
                        path =False

                    run_Look = Look(EndTrack, initial_position=Initial, initial_Forward_move=path)
                    run_Look.add_request(Input_List)
                    look_return, SeekTime = run_Look.schedule()
                    print(look_return, SeekTime)
                    
                    self.Draw_Disk(look_return, EndTrack)
                    
                    self.Result_Label.configure(text=f"Seek Time: {SeekTime}", fg_color="red")
                else:
                    print("Check Input")
    
    def Make_Table(self, Page_list):
        max_rows = max(len(column) for column in Page_list)
        
        for column in Page_list:
            column.extend(['x'] * (max_rows - len(column)))
    
        values = []
        for row in range(max_rows):
            values.append([Page_list[column_index][row] if row < len(Page_list[column_index]) else "" for column_index in range(len(Page_list))])
        
        try:
            if self.table:
                self.table.destroy()
        except:
            pass
        
        self.table = CTkTable(master=self.Solution_Frame, row=max_rows, column=len(Page_list), values=values,width=50)
        self.table.pack(padx=1, pady=1)
            
    def Draw_Disk(self, path_List, end_track):
        self.canvas.delete("all")  
        self.canvas.create_line(20, 30, 800, 30)  
        self.canvas.create_text(20, 10, text="0")

        self.canvas.create_text(800, 10, text=str(end_track))
        
        scale_factor = 780 / end_track
        
        for i, point in enumerate(path_List):
            x = 20 + point * scale_factor
            y = 30
            self.canvas.create_line(x, y - 3, x, y + 3, fill="red", width=2)  
            self.canvas.create_text(x, y + 15, text=str(point))

        prev_x = None
        prev_y = None
        for i, point in enumerate(path_List):
            x = 20 + point * scale_factor
            y = 50 + i * 20  
            self.canvas.create_line(x, y - 3, x, y + 3, fill="red", width=2)  
            self.canvas.create_text(x, y + 15, text=str(point))
            if prev_x is not None and prev_y is not None:
                self.canvas.create_line(prev_x, prev_y, x, y, fill="blue", arrow="last", width=2) 
            prev_x = x
            prev_y = y

    def Algo_Option_Callback(self,c):
        global choice
        choice = c
        if choice == "Optimal" or choice == "Second Chance":
            self.Algo_Label.configure(text="Page Replacement")
            try:
                if self.table:
                    self.table.destroy()
            except:
                pass
            try:
                self.Entry_Size.destroy()
                self.Path_Choice.destroy()
                self.Initial_Position.destroy()
                self.End_line.destroy()
                self.canvas.destroy()
                self.Input_Frame.destroy()
            except:
                pass
            
            self.Entry_Size = customtkinter.CTkEntry(master=self.Main_Frame, placeholder_text="Frame Size", width=100)
            self.Entry_Size.grid(row=3,column=0,pady=10, padx=10)
            # value = [[1,2,3,4,5],
            #         [1,2,3,4,5],
            #         [1,2,3,4,5],
            #         [1,2,3,4,5],
            #         [1,2,3,4,5]]
            # self.table = CTkTable(master=self.Solution_Frame, row=5, column=5, values=value)
            # self.table.pack(expand=True, fill="both", padx=20, pady=20)
            
        elif choice == "C-Scan" or choice == "Look":
            app.geometry("1000x800")
            self.Algo_Label.configure(text="Disk Scheduling")
            try:
                if self.table:
                    self.table.destroy()
            except:
                pass
            try:
                self.Entry_Size.destroy()
                self.Path_Choice.destroy()
                self.Initial_Position.destroy()
                self.End_line.destroy()
                self.canvas.destroy()
                self.Input_Frame.destroy()
            except:
                pass
            
            self.Path_Choice = customtkinter.CTkSegmentedButton(master=self.Main_Frame, values=["Left", "Right"])
            self.Path_Choice.grid(row=3,column=0,pady=10, padx=10)
            
            self.Input_Frame = customtkinter.CTkFrame(master=self.Main_Frame)
            self.Input_Frame.grid(row=4,column=0,pady=10, padx=40)
            
            self.Initial_Position = customtkinter.CTkEntry(master=self.Input_Frame, placeholder_text="Initial Position", width=100)
            self.Initial_Position.grid(row=0,column=0,pady=10, padx=10)
            
            self.End_line = customtkinter.CTkEntry(master=self.Input_Frame, placeholder_text="Range Ending", width=100)
            self.End_line.grid(row=0,column=1,pady=10, padx=10)
            
            self.canvas = customtkinter.CTkCanvas(self.Solution_Frame, width=809, height=400)
            self.canvas.grid(row=0, column=0,padx=20,pady=10)    
            
            

    def Main_Screen(self):
        self.Main_Frame = customtkinter.CTkFrame(master=app)
        self.Main_Frame.pack(pady=20, padx=40)

        self.Algo_Label = customtkinter.CTkLabel(master=self.Main_Frame, justify=customtkinter.LEFT,text="Algorithms",font=("System", 30, "bold"))
        self.Algo_Label.grid(row=0,column=0,pady=10, padx=10)

        self.Algo_Option = customtkinter.CTkOptionMenu(self.Main_Frame, values=["Optimal", "Second Chance", "C-Scan", "Look"],command=self.Algo_Option_Callback)
        self.Algo_Option.grid(row=1,column=0,pady=10, padx=10)
        self.Algo_Option.set("Choose Algorithm")

        self.Entry_Values = customtkinter.CTkEntry(master=self.Main_Frame, placeholder_text="Enter Values...", width=300)
        self.Entry_Values.grid(row=2,column=0,pady=10, padx=10)

        self.Load_Btn = customtkinter.CTkButton(master=self.Main_Frame, command=self.Run_Algo, text="Run")
        self.Load_Btn.grid(row=5,column=0,pady=10, padx=10)
        
        self.Result_Label = customtkinter.CTkLabel(master=self.Main_Frame,text="",font=("System", 30, "bold"))
        self.Result_Label.grid(row=5,column=1,pady=10, padx=10)

        self.Solution_Frame = customtkinter.CTkFrame(master=self.Main_Frame)
        self.Solution_Frame.grid(row=6,column=0,pady=10, padx=10)
        

gui = MainGUI()
gui.Main_Screen()
app.mainloop()
