$(VERBOSE).SILENT:

CC = g++
CFLAGS = -std=c++11 

inc = include
src = source

OBJS = main.o Command.o Controller.o MusicList.o

COMMAND = $(inc)/Command.hpp $(src)/Command.cpp
CONTROLLER = $(inc)/Controller.hpp $(src)/Controller.cpp
FORMAT = $(inc)/Format.hpp
MAIN = ./main.cpp
MUSICLIST = $(inc)/MusicList.hpp $(src)/MusicList.cpp
STRS = $(inc)/Strs.hpp

MusicController : $(OBJS)
	$(CC) $(CFLAGS) -o MusicController $(OBJS)
	@echo Building MusicController...
	
main.o : $(MAIN) $(COMMAND) $(CONTROLLER) $(FORMAT)
	$(CC) $(CFLAGS) -I $(inc) -c $(MAIN) $(COMMAND) $(CONTROLLER) $(FORMAT)
	@echo Building Main... 

Command.o : $(COMMAND) $(FORMAT) $(STRS)
	$(CC) $(CFLAGS) -I $(inc) -c $(COMMAND) $(FORMAT) $(STRS)
	@echo Building Command...

Controller.o : $(CONTROLLER) $(FORMAT) $(MUSICLIST)
	$(CC) $(CFLAGS) -I $(inc) -c $(CONTROLLER) $(FORMAT) $(MUSICLIST)
	@echo Building Controller...

MusicList.o : $(MUSICLIST) $(STRS) $(FORMAT)
	$(CC) $(CFLAGS) -I $(inc) -c $(MUSICLIST) $(STRS) $(FORMAT)
	@echo Building MusicList...

clean :
	rm MusicController $(OBJS) $(inc)/*.gch
	@echo Cleaning...