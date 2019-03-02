import tkinter as tk
import time
import _thread
window = tk.Tk()
window.title("my window")
window.geometry("400x300")
e = tk.Entry(window, show=None)
e.pack()

t = tk.Text(window, height=10, relief="sunken")
t.pack()
in_flag=0
def insert_point():
    global in_flag
    in_flag = 0

def insert_end():
    global in_flag
    oo = 0
    in_flag = 1
    while True:
        time.sleep(0.1)
        oo += 1
        if in_flag == 1:
            t.insert("end", "\n" + str(oo))
            t.see(20.0)
        else:
            break
        text_str = t.get(1.0, "end")
        if text_str.count("\n")>15:
            t.delete(1.0, 2.0)

def th():
    _thread.start_new_thread(insert_end, ())

    #t.icursor(len(e.get()))
b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b2 = tk.Button(window, text="insert end", command=th)
b1.pack()
b2.pack()
window.mainloop()

#_thread.start_new_thread(window.mainloop, ())
#window.mainloop()