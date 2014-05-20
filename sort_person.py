#!/usr/bin/env python3
import datetime

class Person(object):
	"""docstring for Person"""
	
	def __init__(self, vorname, name, gebDat):
		self.vorname = vorname
		self.name = name
		self.gebDat = datetime.datetime.strptime(gebDat, '%d.%m.%Y')

	def __repr__(self):
		return 'Person(vorname=' + self.vorname + ', name=' + self.name + ', gebDat=' + self.getGebDatAsString() + ')'

	def sortByVorname(self):
		return self.vorname

	def getGebDatAsString(self):
		return self.gebDat.strftime('%d.%m.%Y')

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

    print ('Spitznamen ermitteln:')
    persons = map(spitzname, persons)
    print (list(map(lambda p: str(p) + '+ spitzname='+p.spitzname, persons)))

def spitzname(person):
	if person.gebDat.year > 1990:
		person.spitzname = 'Jungspund'
	elif person.gebDat.year > 1980:
		person.spitzname = 'Senior'
	elif person.gebDat.year > 1960:
		person.spitzname = 'Oldie'
	else:
		person.spitzname = 'Gruftie'
	return person


main()


		