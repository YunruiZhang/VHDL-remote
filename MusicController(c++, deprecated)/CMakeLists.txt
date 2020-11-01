cmake_minimum_required(VERSION 3.13)
project(MusicController)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_executable(MusicController main.cpp include/Controller.hpp include/MusicList.hpp source/Controller.cpp source/MusicList.cpp source/command.cpp include/Command.hpp include/Strs.hpp include/Format.hpp main.cpp)
