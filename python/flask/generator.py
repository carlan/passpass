import math
import random

class PasswordGenerator(object):
	def __init__(self, amount=1):
		self.TEMPLATE = 'sldlswswswsldls'
		self.LEGEND = {
			"s": '!@$%^&*-_+=:|~?/.;',
			"d": '0123456789',
			"w": 'sister offense temporary sock finish experience issue mouth position deck seminar begin live blonde impound foot ambiguity smile breed lung'.split(),
			"l": 'abcdefghijklmnoprstuvwxyz'
		}
		self.amount = amount

	def generate(self):
		passwords = []

		for word in self.LEGEND['w']:
			word_index = self.LEGEND['w'].index(word)
			word = "".join( random.choice([letter.upper(), letter ]) for letter in word )
			self.LEGEND['w'][word_index] = word

		self.LEGEND['l'] = "".join( random.choice([letter.upper(), letter ]) for letter in self.LEGEND['l'] )

		for number in range(0, self.amount):
			password = ''
			for char in self.TEMPLATE:
				sorteable = self.LEGEND[char]
				picked = sorteable[math.floor(random.random() * len(sorteable))]
				password+=picked
			passwords.append(password)

		return passwords