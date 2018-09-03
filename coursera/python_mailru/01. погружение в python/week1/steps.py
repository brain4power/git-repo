import sys

num_steps = int(sys.argv[1])
spaces = " "*(num_steps-1)
for step in range(num_steps):
    print(spaces+"X"*(step+1))
    spaces = spaces[0:-1]
