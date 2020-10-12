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

void Controller::stop()
{

}

void Controller::next()
{
    int index = 0;
    if (playMode == ORDER_PLAY)
    {
        index = getCurrIndex(musicList) + 1 < 0
                ? getListSize(musicList) + 1
                : 0;
    }
    else if (playMode == RANDOM_PLAY)
    {
        while (index == getCurrIndex(musicList))
        {
            index = rand() % getListSize(musicList);
        }
    }
    setCurrIndex(musicList, index);
}

void Controller::previous()
{
    int index = 0;
    if (playMode == ORDER_PLAY)
    {
        index = getCurrIndex(musicList) - 1 < 0
                ? getListSize(musicList) - 1
                : getCurrIndex(musicList) - 1;
    }
    else if (playMode == RANDOM_PLAY)
    {
        while (index == getCurrIndex(musicList))
        {
            index = rand() % getListSize(musicList);
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

void Controller::setMode(mode m)
{
    playMode = m;
}

int Controller::songsNumber()
{
    return ::getListSize(musicList);
}

const char * Controller::getCurrentMusic()
{
    return ::getCurrentMusic(musicList);
}
