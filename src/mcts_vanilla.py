
from mcts_node import MCTSNode
from random import choice
from math import sqrt, log

num_nodes = 1000
explore_faction = 2.

def traverse_nodes(node, board, state, identity, test_depth):
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
    # current_node = node

    # Set a boolean representing that leaf has not been reached yet
    # board.legal actions is empty or board.is_ended() indicates that you are at the leaf node
    reachedLeaf = board.is_ended(state) # Returns true or false 

    # Main code:
    if (node.untried_actions is None):
        return node

    # Repeat code until leaf is reached
    else:

        for child in node.untried_actions:
    
            # Expand child node
            new_node = expand_leaf(node, board, state, child, test_depth)
            node.child_nodes[child] = new_node 

            # Removes the untried action of the tree node
            node.untried_actions.pop(0)

            # Run traverse_nodes again, going to the child of the current_node
            # The state is changed as well
            traverse_nodes(node.child_nodes[child], board, board.next_state(state, child), identity, test_depth+1)
            node.tree_to_string(100,0)
        
        return
                      
    #while not reachedLeaf:
        # Move to the next child node
        

        # Update what current node is
        # current_node = 
        
    #pass
    # Hint: return leaf_node


def expand_leaf(node, board, state, child_action, test):
    """ Adds a new leaf to the tree by creating a new child node for the given node.

    Args:
        node:   The node for which a child will be added.
        board:  The game setup.
        state:  The state of the game.

    Returns:    The added child node.

    """
    
    # Changes state of board to the next state
    state = board.next_state(state, child_action)

    # Creates a child node
    child_node = MCTSNode(node, child_action, board.legal_actions(state))


    # Setting child node's untried actions.
    #child_node.untried_actions =  
    #node_to_add_to.child_nodes[new_child] =
    print(child_node.parent_action)
    print(test)
    return child_node
    # Returns 
    # Hint: return new_node


def rollout(board, state):
    """ Given the state of the game, the rollout plays out the remainder randomly.

    Args:
        board:  The game setup.
        state:  The state of the game.

    """

    move = random.choice(board.legal_actions(state)) #pick a random move

    rollout_state = board.next_state(state, move) #do the random move

    while((board.is_ended(rollout_state) is not true)): #as long as the game isnt finished

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
        for children in node.child_nodes.values():
            to_add = to_add + find_all_leaves(children, identity)		#add the eventual leaves of those children to the list
        return to_add							#return the list

def is_win(node, board, state, identity):
    board.display(state, node.parent_action)
    print('checking if this is a win, action: ' + board.display_action(node.parent_action))

    if(board.current_player(state) == identity):
        return 1;

    else:
        return -1;








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
        sampled_board = board

        # Start at root
        node = root_node

        # Do MCTS - This is all you!



    # Utilize traverse_nodes()
    # Then expand_leaf()
    #identifying the decision tree

    print("starting to make the tree");

    traverse_nodes(node, board, state, identity_of_bot, 0)

    #Deciding the best move from the established tree

    leaves = find_all_leaves(node, identity)

    for leaf in leaves:
        sampled_board = board
        sampled_state = state
        root = root_node
        sampled_leaf = leaf
        actions = []
        while(sampled_leaf != root):
            actions.append(sampled_leaf.parent_action)
            sampled_leaf = sampled_leaf.parent
        length = ((len(actions))-1)
        while(length >= 0):
            sampled_state = sampled_board.next_state(sampled_state, actions(length))
            length = length-1
        backpropagate(leaf, is_win(leaf, sampled_board, sampled_state, identity_of_bot))


    best_action = (1,1, 1,1, -20)
    for child in root_node.child_nodes.values():
        if(child.wins >= best_action[-1]):
            best_action = (child.parent_action) + (child.wins)
    return best_action[0:-1]




    # Return an action, typically the most frequently used action (from the root) or the action with the best
    # estimated win rate.
    return None
