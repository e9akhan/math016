import solver

def is_solved():
    assert solver.solver(15)

def test_solver():
    assert solver.solver(15) == 26