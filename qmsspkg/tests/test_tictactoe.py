from tictactoe import initialize_board, make_move

def test_initialize_board():
    board = initialize_board()
    assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 
"Board should be initialized with empty spaces"

def test_make_move():
    board = initialize_board()
    success = make_move(board, 0, 0, 'X')
    assert success, "Move should be successful"
    assert board[0][0] == 'X', "The board position should be updated with 
'X'"
    # Test an invalid move (spot already taken)
    success = make_move(board, 0, 0, 'O')
    assert not success, "Move should fail if spot is already taken"

