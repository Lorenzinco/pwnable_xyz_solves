from z3 import *

# Create Z3 bit vector variables
a = BitVec('a', 32)
b = BitVec('b', 32)
c = BitVec('c', 32)
d = BitVec('d', 32)
e = BitVec('e', 32)

# Create solver instance
solver = Solver()

# Add constraint: sum equals product
solver.add(a + b + c + d + e == a * b * c * d * e)

# Check if there's a solution
if solver.check() == sat:
    # If there's a solution, print the values
    model = solver.model()
    print("Solution found:")
    print("a =", model[a].as_long())
    print("b =", model[b].as_long())
    print("c =", model[c].as_long())
    print("d =", model[d].as_long())
    print("e =", model[e].as_long())
else:
    print("No solution found.")
