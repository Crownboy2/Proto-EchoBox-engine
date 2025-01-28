import tkinter as tk

root = tk.Tk()
root.title("Proto-EchoBox engine")

def create_project():
    project_window = tk.Toplevel(root)
    project_window.title("Создать проект")
    
    label = tk.Label(project_window, text="Вот новое окно для создания проекта!")
    label.pack(pady=20, padx=20)

def settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.title("Настройки")
    
    label = tk.Label(settings_window, text="Это окно настроек!")
    label.pack(pady=20, padx=20)

def about_developer():
    about_window = tk.Toplevel(root)
    about_window.title("О разработчике")

    label = tk.Label(about_window, text="Разработчик: @crown_boy2\nМой ТГК: https://t.me/Tyt_Cb ")
    label.pack(pady=20, padx=20)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x_cordinate = int((screen_width / 2) - 200)
y_cordinate = int((screen_height / 2) - 150)

root.geometry(f"{400}x{350}+{x_cordinate}+{y_cordinate}")


button_frame = tk.Frame(root)
button_frame.pack(pady=50, padx=(0, 10), anchor=tk.E)

button1 = tk.Button(button_frame, text="Создать проект", command=create_project)
button1.pack(fill=tk.X, pady=5, padx=10)

button2 = tk.Button(button_frame, text="Настройки", command=settings_window)
button2.pack(fill=tk.X, pady=5, padx=10)

button3 = tk.Button(button_frame, text="О разработчике", command=about_developer)
button3.pack(fill=tk.X, pady=5, padx=10)

exit_button = tk.Button(button_frame, text="Выход", command=root.destroy)
exit_button.pack(fill=tk.X, pady=5, padx=10) 

root.mainloop()