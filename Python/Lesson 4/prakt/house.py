from person import Person


class House:
    def __init__(self, addr):
        self.__address = addr
        self.__residents = []

    def get_address(self):
        return self.__address

    def set_address(self, addr):
        self.__address = addr

    def settle(self, p):
        if isinstance(p, Person):
            self.__residents.append(p)
            p.set_address(self.__address)

    def evictim(self, p):
        if isinstance(p, Person):
            self.__residents.remove(p)
            p.set_address('n/a')

    def show_residents(self):
        print('*'*20)
        print(f"| Address: {self.__address}")
        print("| Residents:")
        for person in self.__residents:
            if isinstance(person, Person):
                print(f"| - {person._name}")