cmake_minimum_required(VERSION 3.17)
project(MusicController)

set(CMAKE_CXX_STANDARD 11)

add_executable(MusicController main.cpp controller/Controller.cpp include/MusicList.h controller/MusicList.cpp)

include_directories(include)
