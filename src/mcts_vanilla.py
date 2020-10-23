
from mcts_node import MCTSNode
from random import choice
from math import sqrt, log

num_nodes = 1000
explore_faction = 2.

def traverse_nodes(node, board, state, identity):
    """ Traverses the tree until the end criterion are met.

    Args:
        node:       A tree node from which the search is traversing.
        board:      The game setup.
        state:      The state of the game.
        identity:   The bot's identity, either 'red' or 'blue'.

    Returns:        A node from which the next stage of the search can proceed.

    """
    leafNodeList = []
    # Start from the parameter node which is the tree node specified
    current_node = node

    # Set a boolean representing that leaf has not been reached yet
    # board.legal actions is empty or board.is_ended() indicates that you are at the leaf node
    reachedLeaf = board.is_ended() # Returns true or false 

    # Repeat code until leaf is reached
    # The leaf node should be the most recent move made by a player
    while not reachedLeaf:
        # Move to the next child node
        # change what current node is?
        # current_node = node.
        
        # Add leaf node to the list

    pass
    # Hint: return leaf_node


def expand_leaf(node, board, state):
    """ Adds a new leaf to the tree by creating a new child node for the given node.

    Args:
        node:   The node for which a child will be added.
        board:  The game setup.
        state:  The state of the game.

    Returns:    The added child node.

    """
    pass
    # Hint: return new_node


def rollout(board, state):
    """ Given the state of the game, the rollout plays out the remainder randomly.

    Args:
        board:  The game setup.
        state:  The state of the game.

    """

    move = random.choice(board.legal_actions(state))

    rollout_state = board.next_state(state, move)

    while(!(board.is_ended(rollout_state))):

        move = random.choice(board.legal_actions(state))
        rollout_state = board.next_state(rollout_state, move)




    pass


def backpropagate(node, won):
    """ Navigates the tree from a leaf node to the root, updating the win and visit count of each node along the path.

    Args:
        node:   A leaf node.
        won:    An indicator of whether the bot won or lost the game.

    """

    if(node.parent == None):
        return
    else:
        node.wins += won
        node.visits +=1
        return backpropagate(node.parent, won)



    pass


def think(board, state):
    """ Performs MCTS by sampling games and calling the appropriate functions to construct the game tree.

    Args:
        board:  The game setup.
        state:  The state of the game.

    Returns:    The action to be taken.

    """
    identity_of_bot = board.current_player(state)
    root_node = MCTSNode(parent=None, parent_action=None, action_list=board.legal_actions(state))

    for step in range(num_nodes):
        # Copy the game for sampling a playthrough
        sampled_game = state

        # Start at root
        node = root_node

        # Do MCTS - This is all you!

    # Return an action, typically the most frequently used action (from the root) or the action with the best
    # estimated win rate.
    return None
