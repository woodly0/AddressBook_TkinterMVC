import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgBox
from typing import Callable


class ViewTab1(ttk.Frame):
    def __init__(self, root):
        super().__init__()
        root.add(self, text="Edit")
        self.root = root
        self.currentId = None  # trying to keep track of the instance

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.labelFont = ("Arial", 14)
        self.entryFont = ("Arial", 14)
        self.padding = {"padx": 5, "pady": 5}

        # labels:
        self.labelFirstName = ttk.Label(self, text="First Name:", font=self.labelFont)
        self.labelFirstName.grid(column=0, row=1, sticky=tk.W, **self.padding)

        self.labelLastName = ttk.Label(self, text="Last Name:", font=self.labelFont)
        self.labelLastName.grid(column=0, row=2, sticky=tk.W, **self.padding)

        self.labelbirthday = ttk.Label(self, text="Birthday:", font=self.labelFont)
        self.labelbirthday.grid(column=0, row=3, sticky=tk.W, **self.padding)

        self.labelStreet = ttk.Label(self, text="Street:", font=self.labelFont)
        self.labelStreet.grid(column=0, row=4, sticky=tk.W, **self.padding)

        self.labelZip = ttk.Label(self, text="ZIP:", font=self.labelFont)
        self.labelZip.grid(column=0, row=5, sticky=tk.W, **self.padding)

        self.labelCity = ttk.Label(self, text="City:", font=self.labelFont)
        self.labelCity.grid(column=0, row=6, sticky=tk.W, **self.padding)

        self.labelCountry = ttk.Label(self, text="Country:", font=self.labelFont)
        self.labelCountry.grid(column=0, row=7, sticky=tk.W, **self.padding)

        self.labelEmail = ttk.Label(self, text="Email:", font=self.labelFont)
        self.labelEmail.grid(column=0, row=8, sticky=tk.W, **self.padding)

        self.labelPhone = ttk.Label(self, text="Phone:", font=self.labelFont)
        self.labelPhone.grid(column=0, row=9, sticky=tk.W, **self.padding)

        # entries:
        self.entryFirstName = ttk.Entry(self, font=self.entryFont)
        self.entryFirstName.grid(column=2, row=1, sticky=tk.E, **self.padding)

        self.entryLastName = ttk.Entry(self, font=self.entryFont)
        self.entryLastName.grid(column=2, row=2, sticky=tk.E, **self.padding)

        self.entryBirthday = ttk.Entry(self, font=self.entryFont)
        self.entryBirthday.grid(column=2, row=3, sticky=tk.E, **self.padding)

        self.entryStreet = ttk.Entry(self, font=self.entryFont)
        self.entryStreet.grid(column=2, row=4, sticky=tk.E, **self.padding)

        self.entryZip = ttk.Entry(self, font=self.entryFont)
        self.entryZip.grid(column=2, row=5, sticky=tk.E, **self.padding)

        self.entryCity = ttk.Entry(self, font=self.entryFont)
        self.entryCity.grid(column=2, row=6, sticky=tk.E, **self.padding)

        self.entryCountry = ttk.Entry(self, font=self.entryFont)
        self.entryCountry.grid(column=2, row=7, sticky=tk.E, **self.padding)

        self.entryEmail = ttk.Entry(self, font=self.entryFont)
        self.entryEmail.grid(column=2, row=8, sticky=tk.E, **self.padding)

        self.entryPhone = ttk.Entry(self, font=self.entryFont)
        self.entryPhone.grid(column=2, row=9, sticky=tk.E, **self.padding)

        # buttons:
        self.buttonSubmit = tk.Button(self, text="Submit", width=15)
        self.buttonSubmit.grid(column=2, row=10, sticky=tk.SE, **self.padding)

        self.buttonClear = tk.Button(self, text="Clear", width=15)
        self.buttonClear.grid(column=2, row=10, sticky=tk.S, **self.padding)

    def hook_controls(self, controller):
        self.controller = controller
        self.buttonClear.configure(command=self.button_clear)
        self.buttonSubmit.configure(command=self.button_submit)

    def _load_single(self, id):
        self._clear_all_entries()
        address = self.controller.load_single_address(id)

        # self.entryFirstName.delete(0, "end")
        self.currentId = address.id
        self.entryFirstName.insert(0, (address.firstName or ""))
        self.entryLastName.insert(0, (address.lastName or ""))
        self.entryBirthday.insert(0, (address.birthday or ""))
        self.entryStreet.insert(0, (address.street or ""))
        self.entryCity.insert(0, (address.city or ""))
        self.entryZip.insert(0, (address.zip or ""))
        self.entryCountry.insert(0, (address.country or ""))
        self.entryEmail.insert(0, (address.email or ""))
        self.entryPhone.insert(0, (address.phone or ""))

    def button_submit(self, event: tk.Event = None):
        print("button submit")

        if self.currentId is not None:
            answer = msgBox.askquestion(
                title="Update",
                message=f"Do you want to change the existing id { self.currentId }?",
                icon="warning",
            )
            if answer == "no":
                return

        input = {
            "id": self.currentId,
            "firstName": str.strip(self.entryFirstName.get()) or None,
            "lastName": str.strip(self.entryLastName.get()) or None,
            "birthday": str.strip(self.entryBirthday.get()) or None,
            "street": str.strip(self.entryStreet.get()) or None,
            "zip": str.strip(self.entryZip.get()) or None,
            "city": str.strip(self.entryCity.get()) or None,
            "country": str.strip(self.entryCountry.get()) or None,
            "email": str.strip(self.entryEmail.get()) or None,
            "phone": str.strip(self.entryPhone.get()) or None,
        }

        if self.controller.submit_input(input):
            msgBox.showinfo(title="Success", message="Input was accepted")
            self._clear_all_entries()
        else:
            msgBox.showerror(title="Nope", message="Input cannot be accepted")

    def button_clear(self):
        self._clear_all_entries()

    def _clear_all_entries(self):
        self.currentId = None
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)


class ViewTab2(ttk.Frame):
    def __init__(self, root):
        super().__init__()
        root.add(self, text="View")

        # self.columnconfigure(0, weight=3)
        # self.columnconfigure(1, weight=1)
        self.padding = {"padx": 5, "pady": 5}

        # create Treeview:
        self.cols = [
            "id",
            "firstName",
            "lastName",
            "birthday",
            "street",
            "zip",
            "city",
            "country",
            "email",
            "phone",
        ]

        self.myTable = ttk.Treeview(
            self, columns=self.cols, show="headings", height=15, selectmode="browse"
        )

        # set headings:
        for col in self.cols:
            self.myTable.column(col, width=75)
            self.myTable.heading(col, text=col)

        self.myTable.grid(row=0, column=0, columnspan=2)

        # buttons:
        self.buttonDelete = tk.Button(self, text="Delete", width=15)
        self.buttonDelete.grid(row=2, column=1, sticky=tk.S, **self.padding)

        self.buttonClose = tk.Button(self, text="Close", width=15, command=exit)
        self.buttonClose.grid(
            row=2, column=1, columnspan=2, sticky=tk.SE, **self.padding
        )

        # scrollbars:
        ys = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.myTable.yview)
        self.myTable["yscrollcommand"] = ys.set
        ys.grid(row=0, column=2, sticky=(tk.N, tk.S, tk.W))

        xs = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.myTable.xview)
        self.myTable["xscrollcommand"] = xs.set
        xs.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N))

    def hook_controls(self, controller):
        self.controller = controller
        self.myTable.bind("<Double-1>", self._dclick_event)
        self.buttonDelete.configure(command=self.button_delete)
        # self.myTable.bind("<<TreeviewSelect>>", self.tree_click_event)
        for col in self.cols:
            self.myTable.heading(
                col,
                # lambdas are pretty usefull alternative to callback functions
                command=lambda _col=col: self._sort_column(_col, False),
            )

    def _sort_column(self, column, reverse):
        print(f"sorting by { column }")
        ids = self.myTable.get_children("")
        # check column data type. This is ugly..
        if self.myTable.set(ids[0], column).isnumeric():
            columnItems = [(int(self.myTable.set(id, column)), id) for id in ids]
        else:
            columnItems = [(self.myTable.set(id, column), id) for id in ids]
        # rearrange items in sorted positions
        columnItems.sort(reverse=reverse)
        for position, (value, id) in enumerate(columnItems):
            self.myTable.move(id, "", position)
        # reverse function next time
        self.myTable.heading(
            column, command=lambda _col=column: self._sort_column(_col, not reverse)
        )

    def hook_callback(self, callback: Callable):
        self.callback_load = callback

    def _dclick_event(self, event: tk.Event = None):
        item = self.myTable.selection()
        if len(item) != 0:
            clickedItem = self.myTable.item(*item)
            id = clickedItem["values"][0]
            print(f"double-clicked on id {id}")
            self.callback_load(id)

    def initialize(self):
        self._show_all()

    def _show_all(self):
        # remove existing items:
        for item in self.myTable.get_children():
            self.myTable.delete(item)

        # populate freshly:
        addresses = self.controller.load_all_addresses()
        # addresses.sort(key=lambda x: x.lastName)
        for address in addresses:
            displayable = [
                address.id,
                address.firstName or "",
                address.lastName or "",
                address.birthday or "",
                address.street or "",
                address.city or "",
                address.zip or "",
                address.country or "",
                address.email or "",
                address.phone or "",
            ]
            self.myTable.insert(parent="", index="end", values=displayable)

    def button_delete(self):
        print("button delete")
        item = self.myTable.selection()
        if len(item) != 0:
            clickedItem = self.myTable.item(*item)
            id = clickedItem["values"][0]

            answer = msgBox.askquestion(
                title="Delete",
                message=f"Are you sure you want to delete id { id }?",
                icon="warning",
            )
            if answer == "yes":
                self.controller.delete_single_address(id)
                self._show_all()


class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = controller.master
        # self.root.geometry("800x400")
        self.padding = {"padx": 5, "pady": 5}

        self.labelTitle = tk.Label(self.root, text="Address Book", font=("Calibri", 32))
        self.labelTitle.grid(row=0, **self.padding)

        self.labelInstructions = tk.Label(
            self.root, text="Double-click on an existing entry in order to modify it."
        )
        self.labelInstructions.grid(row=1, **self.padding)

        # Create notebook with tabs
        self.tabControl = ttk.Notebook(self.root)
        self.tab0 = ViewTab1(self.tabControl)
        self.tab1 = ViewTab2(self.tabControl)

        self.tabControl.grid(row=2, sticky=tk.W, **self.padding)

        self.tab0.hook_controls(self.controller)
        self.tab1.hook_controls(self.controller)
        self.tab1.hook_callback(self.delegate_load)

        # Events:
        self.tabControl.bind("<<NotebookTabChanged>>", self.switch_handler)
        # self.root.bind("<Return>", self.enter_key)  # could be bound to submit button

    def switch_handler(self, event: tk.Event = None):
        tabName = self.tabControl.tab(event.widget.select(), "text")
        print(f"switching to tab { tabName }")
        tabIndex = event.widget.index("current")

        if tabIndex == 1:
            self.tab1.initialize()

    def delegate_load(self, id: int):
        self.tabControl.select(0)
        self.tab0._load_single(id)

    # def enter_key(self, event: tk.Event = None):
    #     print("enter key")
