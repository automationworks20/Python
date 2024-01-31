
def question(answer):
	return answer == '42' or answer.lower() in ['forty-two', 'forty two']

def main():
	user_input = input('What is the Great Question of Life, the Universe and Everything? ')
	if question(user_input.strip()):
		print("Yes")
	else:
		print("No")


main()
