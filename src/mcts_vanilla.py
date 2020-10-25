
from mcts_node import MCTSNode
from random import choice
from math import sqrt, log

num_nodes = 1000
explore_faction = 2.

def traverse_nodes(node, board, state, identity):
    """ Traverses the tree until the end criterion are met.

    Args:
    # state[-3] x box in the turn made
    # state[-2]
    # state[-1] gives us the player
        node:       A tree node from which the search is traversing.
        board:      The game setup.
        state:      The state of the game.
        identity:   The bot's identity, either 'red' or 'blue'.

    Returns:        A node from which the next stage of the search can proceed.

    """
    # Goal:
    # Traverse to the leaf node, given a specifed node of a tree

    # Current Notes:
    # state[-3] x of the bigger box that the player specified
    # state[-2] y of the bigger box that the player specified
    # state[-1] gives the player who just made a move
    # an action is: R C r c, which is x y of a big box and x y within that big box 
    
    # Start from the parameter node which is the tree node specified
    current_node = node

    # Set a boolean representing that leaf has not been reached yet
    # board.legal actions is empty or board.is_ended() indicates that you are at the leaf node
    reachedLeaf = board.is_ended(state) # Returns true or false 

    # Repeat code until leaf is reached
    while not reachedLeaf:
        # Move to the next child node
        

        # Update what current node is
        # current_node = 
        
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

    move = random.choice(board.legal_actions(state)) #pick a random move

    rollout_state = board.next_state(state, move) #do the random move

    while(!(board.is_ended(rollout_state))): #as long as the game isnt finished

        move = random.choice(board.legal_actions(state)) #keep picking random moves
        rollout_state = board.next_state(rollout_state, move) #and keep doing those random moves




    pass


def backpropagate(node, won):
    """ Navigates the tree from a leaf node to the root, updating the win and visit count of each node along the path.

    Args:
        node:   A leaf node.
        won:    An indicator of whether the bot won or lost the game.

    """

    if(node.parent == None): 			#if we are at the root
        return 						#you're done
    else: 					#if we are not at the root
        node.wins += won 				#update the wins value of this node by either adding 1, 0, or -1 depending on if its a win, tie, or loss respectively
        node.visits +=1 				#update visits by adding 1
        return backpropagate(node.parent, won) 		#repeate with the parent of this node



    pass



def find_all_leaves(node, identity):					#return a list of all of the leaves in the tree
    to_add = []								#Make an empty list
    if(node.child_nodes == None):					#if youre at a child node add it to the list and return the list
        to_add.append(node)
        return to_add
    else:								#for every child of the current node
        for children in node.child_nodes
            to_add = to_add + find_all_leaves(children, identity)		#add the eventual leaves of those children to the list
        return to_add							#return the list


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
