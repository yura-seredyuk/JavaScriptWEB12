from person import Person
from house import House

Bob = Person('Bob', 30)
Rob = Person('Rob', 20)

house1 = House("Street 1")
house1.settle(Bob)
house1.settle(Rob)

Bob.description()
Rob.description()

house1.evictim(Rob)
Rob.description()
house1.show_residents()

from datetime import datetime

today = datetime.today()
print(today.date())