# The puzzle consists of three pegs and a stack of disks of different sizes. 
# Initially, all disks are stacked, from largest to smallest, on the first peg. 
# The goal is to move them to the third peg in the same order. There are two rules:

# 1. We can only move one disk at a time.
# 2. We cannot put a larger disk on top of a smaller disk.

def solve_hanoi(num_disks, first_peg, middle_peg, last_peg):
    if num_disks == 1:
        # Base case
        print("Move the top disk from peg {} to peg {}.".format(first_peg, last_peg))
    else:
        # General Case
        # moving a stack from first_peg to middle_peg
        solve_hanoi(num_disks -1, first_peg, last_peg, middle_peg)
        
        # Move disk num_disks from first_peg to last_peg
        solve_hanoi(1, first_peg, middle_peg, last_peg)
        
        # moving a stack of from middle_peg to last_peg
        solve_hanoi(num_disks -1, middle_peg, first_peg, last_peg)
        
solve_hanoi(3, "A", "B", "C")
