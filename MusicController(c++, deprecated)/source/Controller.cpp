//
// Created by Charlie on 2020/10/10.
//

#include "Controller.hpp"


void Controller::play()
{
    PrintSuccess("Played");
}

void Controller::pause()
{
    PrintSuccess("Paused.");
}

void Controller::stop()
{
    PrintSuccess("Stopped.");
}

void Controller::next()
{
    int index = 0;
    if (getListSize(musicList) == 0)
    {
        cout << ERRORINFO "No music in the list." RESETFMT << endl;
        return;
    }
    if (playMode == ORDER_PLAY)
    {
        index = getCurrIndex(musicList) + 1 >= ::getListSize(musicList)
                ? 0
                : getCurrIndex(musicList) + 1;
    }
    else if (playMode == RANDOM_PLAY)
    {
        while (index == getCurrIndex(musicList))
        {
            index = rand() % getListSize(musicList);
        }
    }
    setCurrIndex(musicList, index);
    PrintSuccess("Changed to the next song.");
}

void Controller::previous()
{
    int index = 0;
    if (getListSize(musicList) == 0)
    {
        cout << ERRORINFO "No music in the list." RESETFMT << endl;
        return;
    }
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
    PrintSuccess("Changed to the previous song.");
}

void Controller::volumeUp()
{
    PrintSuccess("Volume increased.");
}

void Controller::volumeDown()
{
    PrintSuccess("Volume deceased.");
}

void Controller::loadMusicFromDir(const char * dir)
{
    loadMusic(musicList, dir);
}

void Controller::setMode(mode m)
{
    playMode = m;
    switch (playMode)
    {
        case ORDER_PLAY:
            PrintSuccess("Music will be played orderly.");
            break;
        case SINGLE_PLAY:
            PrintSuccess("Music will be played circularly.");
            break;
        case RANDOM_PLAY:
            PrintSuccess("Music will be played randomly.");
            break;
    }
}

mode Controller::getMode()
{
return playMode;
}

int Controller::songsAmount()
{
    return ::getListSize(musicList);
}

string Controller::getCurrentMusic()
{
    return ::getCurrMusic(musicList);
}

void Controller::showSongs()
{
    ::showAllMusic(musicList);
}
