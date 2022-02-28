from data.address import Address
from data.iDB import IDB
from data.sql import *


class Model:
    def __init__(self, source: IDB):
        self.db = source
        self.db.executer(create_address_table)

    def load_all(self) -> list[Address]:
        return self.db.executer(get_all_addresses)

    def load_single(self, id: int) -> Address:
        address = self.db.executer(get_address, params={"id": id})
        return address

    def delete_single(self, id: int) -> bool:
        self.db.executer(delete_address, params={"id": id})
        return True

    def add_new(
        self,
        firstName: str,
        lastName: str,
        birthday: str = None,
        street: str = None,
        zip: str = None,
        city: str = None,
        country: str = None,
        email: str = None,
        phone: str = None,
    ) -> bool:

        address = Address(
            None,
            firstName,
            lastName,
            birthday,
            street,
            zip,
            city,
            country,
            email,
            phone,
        )
        self.db.executer(insert_address, params={"entry": address})
        return True

    def update_existing(
        self,
        id: str,
        firstName: str,
        lastName: str,
        birthday: str = None,
        street: str = None,
        zip: str = None,
        city: str = None,
        country: str = None,
        email: str = None,
        phone: str = None,
    ) -> bool:

        address = Address(
            id, firstName, lastName, birthday, street, zip, city, country, email, phone
        )
        self.db.executer(update_address, params={"entry": address})
        return True

    # def get_dummy(self):
    #     myList = []
    #     myList.append(
    #         Address.from_csv(
    #             firstName="Töme", lastName="Swagger", birthday="24.09.1956"
    #         )
    #     )
    #     self.addresses = myList

    # idb.create_address_table()
    # for a in myAddresses:
    #     idb.insert_address(a)

    # urs: Address = myDB.executer(get_address, params={"id": 1})
    # myDB.executer(update_address, params={"entry": urs})
