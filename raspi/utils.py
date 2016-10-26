
commands = [
		 'STAY',
		 'COME HERE',
		 'COME',
		 'DOWN',
		 'BAD BOY',
		 'HIGH FIVE',
		 'GET OUT',
		 'GOOD BOY',
		 'HELLO',
		 'PUPPY',
		 'SIT',
		 'UP'
]
values = ['a','s','d','f','g','h','j','k','l','z','x','c']

def getCommand(phrase, commands=commands):
	for i in range(len(commands)):
		if phrase.find(commands[i]) != -1:
			return (commands[i],values[i])