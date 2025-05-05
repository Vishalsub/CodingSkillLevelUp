cmake_minimum_required(VERSION 3.10)
project(SoloLeveling)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_executable(test_suite
    tests/test_two_sum.cpp
    src/two_sum.cpp
)
