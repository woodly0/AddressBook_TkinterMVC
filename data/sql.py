from .address import Address
from sqlite3 import Cursor


def create_address_table(cursor: Cursor) -> None:
    # SQLite automatically makes `integer primary key` row auto-incrementing
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS addresses (
                id integer primary key, 
                firstName text, 
                lastName text,
                birthday text,
                street text,
                zip integer,
                city text,
                country text,
                email text,
                phone text
                )"""
    )


def get_all_addresses(cursor: Cursor) -> list[Address]:
    cursor.execute("SELECT * FROM addresses")
    data = cursor.fetchall()
    addresses = []
    for a in data:
        addresses.append(Address(*a))
    return addresses


def insert_address(cursor: Cursor, entry: Address):
    cursor.execute(
        "INSERT INTO addresses (firstName, lastName, birthday, street, zip, city, country, email, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        entry.list_attr_without_id(),
    )


def get_address(cursor: Cursor, id: int) -> Address:
    cursor.execute("SELECT * FROM addresses WHERE id=?", (id,))
    data = cursor.fetchone()
    address = Address(*data)
    return address


def update_address(cursor: Cursor, entry: Address):
    params = entry.__dict__
    cursor.execute(
        """UPDATE addresses SET 
            firstName=:firstName, 
            lastName=:lastName, 
            birthday=:_birthday, 
            street=:street, 
            zip=:zip, 
            city=:city, 
            country=:country, 
            email=:email, 
            phone=:phone 
        WHERE id=:id""",
        params,
    )


def delete_address(cursor: Cursor, id: int):
    cursor.execute("DELETE FROM addresses WHERE id=?", (id,))
