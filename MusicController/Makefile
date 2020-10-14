CC = g++
CFLAGS = -std=c++11

inc = include

OBJS = main.o Command.o Controller.o MusicList.o

COMMAND = include/Command.hpp source/Command.cpp
CONTROLLER = include/Controller.hpp source/Controller.cpp
FORMAT = include/Format.hpp
MUSICLIST = include/MusicList.hpp source/MusicList.cpp
STRS = include/Strs.hpp

MusicController : $(OBJS)
	$(CC) $(CFLAGS) -o MusicController $(OBJS)

main.o : main.cpp $(COMMAND) $(CONTROLLER) $(FORMAT)
	$(CC) $(CFLAGS) -I $(inc) -c main.cpp $(COMMAND) $(CONTROLLER) $(FORMAT)

Command.o : $(COMMAND) $(FORMAT) $(STRS)
	$(CC) $(CFLAGS) -I $(inc) -c $(COMMAND) $(FORMAT) $(STRS)

Controller.o : $(CONTROLLER) $(FORMAT) $(MUSICLIST)
	$(CC) $(CFLAGS) -I $(inc) -c $(CONTROLLER) $(FORMAT) $(MUSICLIST)

MusicList.o : $(MUSICLIST) $(STRS) $(FORMAT)
	$(CC) $(CFLAGS) -I $(inc) -c $(MUSICLIST) $(STRS) $(FORMAT)

clean : 
	rm MusicController $(OBJS) $(inc)/*.gch