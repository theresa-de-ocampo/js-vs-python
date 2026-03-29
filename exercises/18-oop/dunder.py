class Location:
    def __init__(self, country: str) -> None:
        self.country = country

    def __repr__(self) -> str:
        return f"Location(country={self.country})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):
            # Why not just return False?
            # False: "I compared them, and they are NOT equal."
            # NotImplemented: "I don't know how to compare these—ask the other object."
            return NotImplemented
        return other.country == self.country


ph = Location("Philippines")
print(ph)

ph_dict = {"country": "Philippines"}
print(ph == ph_dict)
