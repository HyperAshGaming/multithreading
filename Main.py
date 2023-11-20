import tkinter as tk

def toggle_frame():
    global current_frame
    current_frame.grid_forget()
    if current_frame is red_frame:
        blue_frame.grid(row=0, column=0, padx=10, pady=10)
        current_frame = blue_frame
    else:
        red_frame.grid(row=0, column=0, padx=10, pady=10)
        current_frame = red_frame


# Create the root window
root = tk.Tk()


# Create the initial frames
red_frame = tk.Frame(root, width=200, height=200, bg='red')
blue_frame = tk.Frame(root, width=200, height=200, bg='blue')


# Initially, display the red frame
current_frame = red_frame
red_frame.grid(row=0, column=0, padx=10, pady=10)


# Create a button to toggle between frames
button = tk.Button(root, text='Toggle Frame', command=toggle_frame)
button.grid(row=1, column=0, padx=10, pady=10)


root.mainloop()