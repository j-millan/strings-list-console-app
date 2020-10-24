import re

strings = list()
commands = dict()

def separators(func):
	def deco():
		print('--  --  --  --  --  --  --  --  --  -- --  --  --  --  --  --')
		func()
		print('--  --  --  --  --  --  --  --  --  -- --  --  --  --  --  --')

	return deco

#------------------------------- COMMAND FUNCTIONS ---------------------------------------------

@separators
def list_strings():
	for s in strings:
		print(f' - {s}')

def add(word):
	words = list(map(lambda s: s.lower(), strings))
	if word.lower() in words:
		print(f'"{word}" is already in the list.')
	elif len(word) < 2:
		print(f'The word must at least have two characters.')
	else:
		strings.append(word)

def uppercase(word):
	for i,w in enumerate(strings):
		if w == word:
			strings[i] = word.upper()
			return

	print(f'"{word}" could not be found in the list.')

def uppercaseall():
	global strings
	strings = list(map(lambda s: s.upper(), strings))

def sort():
	strings.sort()

@separators
def help():
	for key in commands:
		command = commands[key]
		print(f'{key}: {command[1]}')

#------------------------------- COMMAND DICTIONARY ---------------------------------------------

commands = {
	'/list': (list_strings, 'Lists all the strings in the list.'), 
	'/sort': (sort, 'Sorts all the strings in the list alphabetically.'),
	'/add': (add, 'Lets the user input a new string and adds it to the list.'),
	'/uppercase': (uppercase, 'Uppercases the input word if found in the list.'),
	'/uppercaseall': (uppercaseall, 'Uppercases all the words in the list.'),
	'/help': (help, 'Lists all the avaliable commands.'),
}

#------------------------------- MAIN PROGRAM LOOP ---------------------------------------------

while True:
	print('Insert a command...')
	string = input()
	command = re.search('^/[a-z]+', string)
	if command:
		try:
			item =	commands[command.group()]
			func = item[0]
			argument = re.search(r'\s[a-zA-Z]+$', string)
			if argument:
				try:
					func(argument.group().strip())
				except TypeError:
					print('This command does not accept any arguments')
			else:
				try:
					func()
				except TypeError:
					print('This command requires an argument.')

		except KeyError:
			print('That is not a valid command')