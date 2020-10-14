//
// Created by Charlie on 2020/10/10.
//

#include <cstdlib>

#include "Format.hpp"
#include "MusicList.hpp"

#ifndef MUSICCONTROLLER_CONTROLLER_HPP
#define MUSICCONTROLLER_CONTROLLER_HPP

enum mode {SINGLE_PLAY, ORDER_PLAY, RANDOM_PLAY};

class Controller
{
private:
    MusicList musicList = newMusicList();
    mode playMode = ORDER_PLAY;

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
    mode getMode();
    int  songsAmount();
    string getCurrentMusic();
    void showSongs();
};


#endif //MUSICCONTROLLER_CONTROLLER_H
