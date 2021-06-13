from board import Board
#from helperFunctions import *

def main():
	# init board
	board = Board()

	while (True):

		# singles
		board.find_hidden_singles()
		board.set_obvious_singles()

		if (board.iscomplete()):
			break

		# doubles
		board.find_hidden_doubles()
		board.set_obvious_doubles()
		# singles
		board.find_hidden_singles()
		board.set_obvious_singles()

		if (board.iscomplete()):
			break

		# triples
		board.find_hidden_triples()
		board.set_obvious_triples()
		# doubles
		board.find_hidden_doubles()
		board.set_obvious_doubles()

	# end While loop

	print(board)

# end Main function


if __name__ == "__main__":
    main()


# exec(open("C:/Users/********/Documents/Sudoku/main.py").read())