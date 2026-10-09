class Person:
  def __init__(self, name, age, occupation, nationality = "Canadian"):
    self.name = name
    self.age = age
    self.occupation = occupation
    self.nationality = nationality

  def setName(self, name):
    self.name = name

  def setAge(self, age):
    self.age = age

  def setOccupation(self, occupation):
    self.occupation = occupation

  def setNationality(self, nationality):
    self.nationality = nationality

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

  def getOccupation(self):
    return self.occupation

  def getNationality(self):
    return self.nationality

  def description(self):
    print(self.name, "is", self.age, "years old. They are", self.nationality + ", and work as a", self.occupation)


Selena = Person("Selena", "6", "n/a", "Chinese")
Selena.description()

Samuel = Person("Samuel", "11", "n/a", "Chinese")
Samuel.description()

Ma = Person("Kristen", "42", "something at UBC", "Chinese")
Ma.description()

Dad = Person("Kai", "45?", "something in chinese", "Chinese")
Dad.description()

