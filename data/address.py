from datetime import date
import dateutil.parser


class Address:
    def __init__(
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
    ):
        self.id = int(id) if not id is None else None
        self.firstName = firstName
        self.lastName = lastName
        self._birthday: date = (
            dateutil.parser.parse(birthday).date() if not birthday is None else None
        )
        self.street = street
        self.zip = int(zip) if not zip is None else None
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"<Address> with id { self.id }"

    @property
    def birthday(self):
        return (
            self._birthday.strftime("%d.%m.%Y") if not self._birthday is None else None
        )

    def list_attr_without_id(self):
        return [
            self.firstName,
            self.lastName,
            self.birthday,
            self.street,
            self.zip,
            self.city,
            self.country,
            self.email,
            self.phone,
        ]

    # def list_attr_with_id(self):
    #     return [
    #         self.id,
    #         self.firstName,
    #         self.lastName,
    #         self.birthday,
    #         self.street,
    #         self.zip,
    #         self.city,
    #         self.country,
    #         self.email,
    #         self.phone,
    #     ]

    # @classmethod
    # def without_id(
    #     cls,
    #     firstName: str,
    #     lastName: str,
    #     birthday: str = None,
    #     street: str = None,
    #     zip: str = None,
    #     city: str = None,
    #     country: str = None,
    #     email: str = None,
    #     phone: str = None,
    # ):
    #     birthday = (
    # # datetime.fromisoformat(birthday).date() if not birthday is None else None
    #         date.isoformat(datetime.strptime(birthday, "%d.%m.%Y"))
    #         if not birthday is None
    #         else None
    #     )

    #     return cls(
    #         None,
    #         firstName,
    #         lastName,
    #         birthday,
    #         street,
    #         zip,
    #         city,
    #         country,
    #         email,
    #         phone,
    #     )
