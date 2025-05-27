#include "two_sum.hpp"
#include <gtest/gtest.h>

// 🔽 ADD these includes for std::vector
#include <vector>

TEST(TwoSumTest, BasicCase) {
    Solution s;
    std::vector<int> nums = {2, 7, 11, 15};
    std::vector<int> result = s.twoSum(nums, 9);
    EXPECT_EQ(result, std::vector<int>({0, 1}));
}
