## Credits to https://www.youtube.com/watch?v=1L5zPhhUVic 
## We also used ChatGpt to fix bugs and errors.
import tkinterweb
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime


def open_link(url2):
    url = "https://www.google.com"  
    webbrowser.open(url2)


def exit_fullscreen(event=None):
    window.attributes('-fullscreen', False)
    window.geometry("750x750")  


window = Tk()
window.config(bg="#2e2e2e")
window.title("EfficienZ")
window.geometry("500x500")  
window.attributes("-fullscreen", True)


sidebar = Frame(window, bg="#373737", width=200, height=500)
sidebar.pack(side="left", fill="y")  


button_style = {"bg": "#4CAF50", "fg": "white", "width": 5, "height": 3}


gmail_Button_Image = Image.open("images/Gmail.png")
gmail_Button_Image2 = ImageTk.PhotoImage(gmail_Button_Image)
gmail_button = Button(sidebar, image=gmail_Button_Image2, text="Gmail", command=lambda: open_link("https://gmail.com"), width=50, height=50, bg="#373737", bd=0)
gmail_button.pack(pady=10)


docs_Button_Image = Image.open("images/GCL.png")
docs_Button_Image2 = ImageTk.PhotoImage(docs_Button_Image)
docs_button = Button(sidebar, image=docs_Button_Image2, text="Google Docs", command=lambda: open_link("https://docs.google.com"), width=50, height=50, bg="#373737", bd=0)
docs_button.pack(pady=10)


drive_Button_Image = Image.open("images/GDriveL.png")
drive_Button_Image2 = ImageTk.PhotoImage(drive_Button_Image)
drive_button = Button(sidebar, image=drive_Button_Image2, text="Google Drive", command=lambda: open_link("https://drive.google.com"), width=50, height=50, bg="#373737", bd=0)
drive_button.pack(pady=10)


#Add Shortcut Button
add_Button_Image = Image.open("images/AddApp.png")
add_Button_Image2 = ImageTk.PhotoImage(add_Button_Image)
add_button = Button(sidebar, text="+", command=lambda: open_link("https://workspace.google.com"), width=2, height=2, bg="#373737", bd=0, font="Arial", fg="white")
add_button.pack(pady=10)


from datetime import datetime, timedelta


class TaskManager:
    def __init__(self, window):
       
        web = tkinterweb.HtmlFrame(window)
        web.load_website("https://google.com")
        web.pack(side=LEFT, anchor="nw")


        # Title Settings
        self.setting_title = Label(window, text="Settings", bg="#2e2e2e", fg="white", bd=0, font=("Arial", 20), width=8)
        self.setting_title.pack(side=TOP, anchor="ne")


        # Dark Mode
        self.add_task_button = Button(window, text="Dark Mode", command=self.dark_mode, bg="#2e2e2e", fg= "white", width=15)
        self.add_task_button.pack(side=TOP, anchor="ne")


        # Blue Mode
        self.add_task_button = Button(window, text="Blue Mode", command=self.blue_mode, bg="#38b6ff", fg= "white", width=15)
        self.add_task_button.pack(side=TOP, anchor="ne")


        # White Mode
        self.add_task_button = Button(window, text="Light Mode", command=self.light_mode, bg="white", fg= "black", width=15)
        self.add_task_button.pack(side=TOP, anchor="ne")


        # Gold Mode
        self.add_task_button = Button(window, text="Gold Mode", command=self.light_mode, bg="yellow", fg= "black", width=15)
        self.add_task_button.pack(side=TOP, anchor="ne")




        # Task List
        self.task_list_frame = Frame(window, bg="#2e2e2e", bd=0)
        self.task_list_frame.pack(side=BOTTOM, padx=10, pady=10, anchor="se")


        self.task_list = Listbox(self.task_list_frame, width=50, height=25, bg="#2e2e2e", fg= "white", bd=0)
        self.task_list.pack()


        # Points
        self.points = 0
        self.points_label = Label(window, text=f"Points: {self.points}", font=("Arial", 14), bg="#2e2e2e", fg= "white", bd=0)
        self.points_label.pack(side=TOP, anchor='ne')


        # Title
        self.task_title = Label(window, text="Create Task: ", bg="#2e2e2e", fg="white", bd=0, font=("Arial", 17), width=25)
        self.task_title.pack(side=TOP, anchor="ne")


        # Frame for Task Creation
        self.task_frame = Frame(window, bg="#2e2e2e")
        self.task_frame.pack(side=RIGHT, padx=10, pady=10)


        # Task Name
        self.task_label = Label(self.task_frame, text="Task Name:", bg="#2e2e2e", fg= "white", bd=0, width=45)
        self.task_label.pack()
        self.task_entry = Entry(self.task_frame, bg="#2e2e2e", fg= "white", width=45)
        self.task_entry.pack()


        # Priority
        self.priority_label = Label(self.task_frame, text="Priority (1-5):", bg="#2e2e2e", fg= "white", bd=0, width=45)
        self.priority_label.pack()
        self.priority_entry = Entry(self.task_frame, bg="#2e2e2e", fg= "white", width=45)
        self.priority_entry.pack()


        # Due Date
        self.due_date_label = Label(self.task_frame, text="Due Date (D-H-M):", bg="#2e2e2e", fg= "white", bd=0, width=45)
        self.due_date_label.pack()
        self.due_date_entry = Entry(self.task_frame, bg="#2e2e2e", fg= "white", width=45)
        self.due_date_entry.pack()


        # Add Task Button
        self.add_task_button = Button(self.task_frame, text="Add Task", command=self.add_task, bg="#2e2e2e", fg= "white", width=35)
        self.add_task_button.pack()


    def dark_mode(self):
        self.task_entry.config(bg="#2e2e2e", fg="white")
        self.task_frame.config(bg="#2e2e2e")
        self.task_label.config(bg="#2e2e2e", fg="white")
        self.task_list.config(bg="#2e2e2e")
        self.task_list_frame.config(bg="#2e2e2e")
        self.task_title.config(bg="#2e2e2e", fg="white")
        self.add_task_button.config(bg="#2e2e2e", fg="white")
        self.due_date_entry.config(bg="#2e2e2e", fg="white")
        self.due_date_label.config(bg="#2e2e2e", fg="white")
        self.priority_entry.config(bg="#2e2e2e", fg="white")
        self.priority_label.config(bg="#2e2e2e", fg="white")
        self.setting_title.config(bg="#2e2e2e", fg="white")
        self.points_label.config(bg="#2e2e2e", fg="white")
        window.config(bg="#2e2e2e")
        sidebar.config(bg="#373737")
        drive_button.config(bg="#373737")
        docs_button.config(bg="#373737")
        gmail_button.config(bg="#373737")
        add_button.config(bg="#373737")


    def blue_mode(self):
        self.task_entry.config(bg="#2e2e2e", fg="white")
        self.task_frame.config(bg="#38b6ff")
        self.task_label.config(bg="#2e2e2e", fg="white")
        self.task_list.config(bg="#2e2e2e")
        self.task_list_frame.config(bg="#2e2e2e")
        self.task_title.config(bg="#38b6ff", fg="white")
        self.add_task_button.config(bg="#2e2e2e", fg="white")
        self.due_date_entry.config(bg="#2e2e2e", fg="white")
        self.due_date_label.config(bg="#2e2e2e", fg="white")
        self.priority_entry.config(bg="#2e2e2e", fg="white")
        self.priority_label.config(bg="#2e2e2e", fg="white")
        self.setting_title.config(bg="#2e2e2e", fg="white")
        self.points_label.config(bg="#2e2e2e", fg="white")
        window.config(bg="#38b6ff")
        sidebar.config(bg="#0cc0df")
        drive_button.config(bg="#0cc0df")
        docs_button.config(bg="#0cc0df")
        gmail_button.config(bg="#0cc0df")
        add_button.config(bg="#0cc0df")


    def light_mode(self):
        self.task_entry.config(bg="white", fg="#2e2e2e")
        self.task_frame.config(bg="white")
        self.task_label.config(bg="white", fg="#2e2e2e")
        self.task_list.config(bg="white")
        self.task_list_frame.config(bg="white")
        self.task_title.config(bg="white", fg="#2e2e2e")
        self.add_task_button.config(bg="white", fg="#2e2e2e")
        self.due_date_entry.config(bg="white", fg="#2e2e2e")
        self.due_date_label.config(bg="white", fg="#2e2e2e")
        self.priority_entry.config(bg="white", fg="#2e2e2e")
        self.priority_label.config(bg="white", fg="#2e2e2e")
        self.setting_title.config(bg="white", fg="#2e2e2e")
        self.points_label.config(bg="white", fg="#2e2e2e")
        window.config(bg="white")
        sidebar.config(bg="#DCDCDC")
        drive_button.config(bg="#DCDCDC")
        docs_button.config(bg="#DCDCDC")
        gmail_button.config(bg="#DCDCDC")
        add_button.config(bg="#DCDCDC")


    def add_task(self):
        task_name = self.task_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()


        # Validate inputs
        if not task_name or not priority or not due_date:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return


        try:
            priority = int(priority)
            if priority < 1 or priority > 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Priority must be an integer between 1 and 5.")
            return


        try:
            days, hours, minutes = map(int, due_date.split('-'))
            due_time = datetime.now() + timedelta(days=days, hours=hours, minutes=minutes)
        except ValueError:
            messagebox.showerror("Input Error", "Due date must be in D-H-M format.")
            return


        # Add task to list
        task_info = f"{task_name} | Priority: {priority} | Due: {due_time.strftime('%Y-%m-%d %H:%M')}"
        self.task_list.insert(END, task_info)


        # Create a finish button for the task
        finish_button = Button(self.task_list_frame, text="Finish", command=lambda: self.finish_task(task_info, priority))
        finish_button.pack(side=TOP, anchor='w')


        # Clear input fields
        self.task_entry.delete(0, END)
        self.priority_entry.delete(0, END)
        self.due_date_entry.delete(0, END)


    def finish_task(self, task_info, priority):
        # Calculate points
        points_awarded = priority * 10
        self.points += points_awarded
        self.points_label.config(text=f"Points: {self.points}")


        # Remove the task from the list
        index = self.task_list.get(0, END).index(task_info)
        self.task_list.delete(index)


        # Remove the corresponding finish button
        for widget in self.task_list_frame.winfo_children():
            if isinstance(widget, Button) and widget['text'] == "Finish":
                widget.destroy()
                break


# Create the main content frame to hold the button for the link
main_content = Frame(window, bg="#2e2e2e")
main_content.pack(fill="both", expand=True)


window.bind('<Escape>', exit_fullscreen)


task_manager = TaskManager(window)


# Run the Tkinter event loop
window.mainloop()
