#include "leetcode/two_sum.hpp"
#include <iostream>
#include <cassert>

int main() {
    TwoSum solver;
    auto result = solver.solve({2, 7, 11, 15}, 9);
    assert(result[0] == 0 && result[1] == 1);
    std::cout << "test_two_sum passed.\n";
    return 0;
}
