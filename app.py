import tkinter as tk
from gui.controller import Controller

# TODO: Should probalby create a seperate Address class for the GUI part
# TODO: Style the notebook table. It's rather ugly to look at.


class App(tk.Tk):
    """
    Tkinter based GUI app. Trying to implement the MVC pattern, which means that
    the controller knows everything, the view doesn't know anything about the model
    and the model knows nothing about the other two.
    """

    def __init__(self):
        super().__init__()
        self.version = "1.0"
        self.title(f"Address Book v{ self.version }")

        # add icon:
        icon = tk.PhotoImage(file="img/book_icon.png")
        self.iconphoto(True, icon)

        # load controller:
        self.controller = Controller(self)


if __name__ == "__main__":
    print("Start...")
    app = App()
    app.mainloop()
    print("exit.")
