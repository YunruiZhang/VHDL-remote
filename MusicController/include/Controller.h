//
// Created by Charlie on 2020/10/10.
//

#include <cstdlib>
#include "MusicList.h"
#ifndef MUSICCONTROLLER_CONTROLLER_H
#define MUSICCONTROLLER_CONTROLLER_H

enum mode {SINGLE_PLAY, ORDER_PLAY, RANDOM_PLAY};

typedef struct music * Music;

class Controller
{
private:
    MusicList musicList = newMusicList();
    int playMode = ORDER_PLAY;
public:
    void play();
    void pause();
    void stop();
    void next();
    void previous();
    void volumeUp();
    void volumeDown();
    void loadMusicFromDir(const char *);
    void setMode(mode);
    int  songsNumber();
    const char * getCurrentMusic();
};


#endif //MUSICCONTROLLER_CONTROLLER_H
