cmake_minimum_required(VERSION 3.13)
project(MusicController)

set(CMAKE_CXX_STANDARD 11)

include_directories(include)

add_executable(MusicController main.cpp include/Controller.h include/dirent.h include/Interface.h include/MusicList.h source/Controller.cpp source/Interface.cpp source/MusicList.cpp)


