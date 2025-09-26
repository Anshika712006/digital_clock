import tkinter as tk
from time import strftime

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="black")

# Function to update the clock
def update_time():
    time_string = strftime('%I:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=time_string)
    label.after(1000, update_time)  # Update every 1000ms (1 second)

# Create a label to display the time
label = tk.Label(root, font=('calibri', 60, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center', expand=True)

# Start the clock
update_time()

# Run the application
root.mainloop()
