# The decreasing number game begins with a float _n_.
# In each turn, there are two possible moves: subtract 1 from the number, or divide it by 2.
# The game ends when the number drops below 1.
# For a starting value _n_, how many possible sequences of moves are there?

starting_num = int(input("Enter the starting value for GamePath: "))

# a recursive function to compute the number of paths in the decreasing numbers game

def game_paths(n):
    if n < 1:
        return 1
    else:
        return game_paths(n-1) + game_paths(n/2)

print(game_paths(starting_num))