cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(Task2 VERSION 1.0)

add_executable(Task2 main.cpp shape.cpp circle.cpp container.cpp rectangle.cpp triangle.cpp constants.h)