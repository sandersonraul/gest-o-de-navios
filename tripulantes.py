class CrewTable:
    def __init__(self, size=50):
        self.size = size
        self.table = [None] * size

    def hash_function(self, code):
        return code % self.size

    def add_crew_member(self, code, name, age):
        index = self.hash_function(code)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (code, name, age)

    def find_crew_member(self, code):
        index = self.hash_function(code)
        while self.table[index] is not None:
            if self.table[index][0] == code:
                return self.table[index]
            index = (index + 1) % self.size
        return None

crew_table = CrewTable()

crew_data = [(1, "John Smith", 30), (2, "Jane Doe", 25), (3, "Bob Johnson", 35)]

for code, name, age in crew_data:
    crew_table.add_crew_member(code, name, age)

x = 3
crew_member = crew_table.find_crew_member(x)
if crew_member:
    print("Crew member found:")
    print("Code:", crew_member[0])
    print("Name:", crew_member[1])
    print("Age:", crew_member[2])
else:
    print("Crew member not found.")