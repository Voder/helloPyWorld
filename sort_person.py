#!/usr/bin/env python3

class Person(object):
	"""docstring for Person"""
	
	def __init__(self, vorname, name, gebDat):
		self.vorname = vorname
		self.name = name
		self.gebDat = gebDat

	def __repr__(self):
		return 'Person(vorname=' + self.vorname + ', name=' + self.name + ', gebDat=' + self.gebDat + ')'

	def sortByVorname(self):
		return self.vorname

def main():
    p1 = Person('Hans', 'Wurst', '01.01.1990')
    # print(p1)
    p2 = Person('Sepp', 'Kaese', '01.06.1995')
    # print(p2)
    p3 = Person('Karl', 'Brot', '01.03.1970')
    # print(p3)
    p4 = Person('John', 'Bier', '01.01.1980')
    # print(p4)

    persons = [p1, p2, p3, p4]
    print (persons)

    print('Sorted')
    print (sorted (persons, key=Person.sortByVorname))

def sortByName(person):
	return person.name

main()


		