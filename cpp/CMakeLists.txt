cmake_minimum_required(VERSION 3.10)
project(LeetCodeCpp)

set(CMAKE_CXX_STANDARD 17)
enable_testing()

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/release-1.12.1.zip
)
FetchContent_MakeAvailable(googletest)

include_directories(include)

add_library(two_sum src/two_sum.cpp)

add_executable(run_tests tests/test_two_sum.cpp)
target_link_libraries(run_tests two_sum gtest_main)
