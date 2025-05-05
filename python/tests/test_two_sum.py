from leetcode.two_sum import TwoSum

def test_two_sum():
    solver = TwoSum()
    assert solver.solve([2, 7, 11, 15], 9) == [0, 1]
