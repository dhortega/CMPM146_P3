Teammates: Joshua Brown & Daniel Jarreau Ortega

Modifications done from mcts_vanilla to mcts_modified:

    instead of picking random moves for the rollouts the rollout now picks based on our strategy function
    
    the strategy function takes in the current node, board, and state and compares the state of the board after each 
    of the possible moves have been made. It then decides which move to make by first checking to see if any more boxes
    have been clamed by any of the moves, if a move claims a box it is returned as the most optimal move. Other than that
    if no moves claim a box it checks to see how many possible moves are able to be made for each of the possible next states
    after this comparison it returns the move that leaves the next state with as little possible moves to be made. This 
    strategy takes away our opponent's available options on their turn.
