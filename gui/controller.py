from pathlib import Path
from data.address import Address
from data.iDB import IDB
from gui.model import Model
from gui.view import View


class Controller:
    def __init__(self, master):
        self.master = master

        # load database and create model:
        myDB = IDB(dbPath=Path("data/sqlite.db"))
        self.model = Model(myDB)

        # load view:
        self.view = View(self)

    def load_all_addresses(self) -> list[Address]:
        addresses = self.model.load_all()
        return addresses

    def load_single_address(self, id: int) -> Address:
        address = self.model.load_single(id)
        return address

    def submit_input(self, inputDict: dict) -> bool:
        try:
            address = {k: v for k, v in inputDict.items() if v is not None}
            # address = inputDict
            if "id" in address:
                self.model.update_existing(**address)
            else:
                self.model.add_new(**address)
        except Exception as ex:
            print(ex)
            return False
        return True

    def delete_single_address(self, id: int) -> bool:
        try:
            self.model.delete_single(id)
        except Exception as ex:
            print(ex)
            return False
        return True
