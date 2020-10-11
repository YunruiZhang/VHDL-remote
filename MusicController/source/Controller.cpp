//
// Created by Charlie on 2020/10/10.
//

#include "Controller.h"


void Controller::play()
{

}

void Controller::pause()
{

}

void Controller::next()
{
    int index = 0;
    if (playMode == ORDER_PLAY)
    {
        index = (musicList->curr + 1) % musicList->size;
    }
    else if (playMode == RANDOM_PLAY)
    {
        while (index == musicList->curr)
        {
            index = rand() % musicList->size;
        }
    }
    setCurrIndex(musicList, index);
}

void Controller::previous()
{
    int index = 0;
    if (playMode == ORDER_PLAY)
    {
        index = musicList->curr - 1 < 0
                ? musicList->size - 1
                : musicList->curr - 1;
    }
    else if (playMode == RANDOM_PLAY)
    {
        while (index == musicList->curr)
        {
            index = rand() % musicList->size;
        }
    }
    setCurrIndex(musicList, index);
}

void Controller::volumeUp()
{

}

void Controller::volumeDown()
{

}

void Controller::loadMusicFromDir(const char * dir)
{
    loadMusic(musicList, dir);
}

void Controller::changeMode(mode m)
{
    playMode = m;
}

const char * Controller::getCurrentMusic()
{
    return musicList->music[musicList->curr]->musicName;
}


