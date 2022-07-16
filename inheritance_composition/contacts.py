class Address:
    def __init__(self, street, city, state, zipcode, street2="") -> None:
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    # Dunder str overloads str method so printing an object of this class prints the address in a formatted form
    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)

        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return "\n".join(lines)
