//
// Created by Charlie on 2020/10/10.
//

#include <algorithm>
#include <dirent.h>
#include <iomanip>
#include <utility>

#include "MusicList.hpp"

/**
 * Check if a file is playable by its suffix.
 * @return {@code true} if suffix matches any video or music format, or {@code false} if none
 */
static bool isPlayable(const string&);

MusicList newMusicList()
{
    MusicList m;
    m.curr = -1;
    return m;
}

NodeMusic newNodeMusic(const string& name)
{
    NodeMusic i;
    i.musicName = name;
    return i;
}

int addMusic(MusicList& l, const string& name)
{
    if (!musicExist(l, name) && isPlayable(name))
    {
        l.music.push_back(newNodeMusic(name));
        return 1;
    }
    return 0;
}

void loadMusic(MusicList& l, const char * dir)
{
    DIR * d;
    struct dirent *ent;
    l.music.clear();
    if ((d = opendir(dir)) != nullptr)
    {
        int n = 0;
        while ((ent = readdir(d)) != nullptr)
        {
            n += addMusic(l, ent->d_name);
        }
        cout << SUCCESSINFO << "Loaded " << n << " songs." << endl;
        l.curr = 0;
    }
    else
    {
        PrintError("Failed to open directory: " << dir);
        return;
    }
}

bool musicExist(MusicList l, const string& name)
{
    return musicIndex(std::move(l), name) != -1;
}


int musicIndex(MusicList l, const string& name)
{
    for (int i = 0; i < l.music.size(); i++)
    {
        if (l.music[i].musicName == name)
        {
            return i;
        }
    }
    return -1;
}

void setCurrIndex(MusicList& l, int x)
{
    l.curr = x;
}

static bool isPlayable(const string& name)
{
    string audioFormat[] = {".mp3", ".wav", ".wma", ".m4a", ".aac"};

    for (const auto & i : audioFormat)
    {
        if (hasEnding(name, i)) return true;
    }
    
    return false;
}

int getCurrIndex(const MusicList& l)
{
    return l.curr;
}

string getCurrMusic(MusicList l)
{
    return l.music[l.curr].musicName;
}

int getListSize(const MusicList& l)
{
    return l.music.size();
}

void showAllMusic(MusicList l)
{
    if (l.music.empty())
    {
        cout << "None." << endl;
        return;
    }

    for (int i = 0; i < l.music.size(); i++)
    {
        if (i == l.curr)
        {
            cout << setfill(' ') << setw(3) << i << ": " INVERSE << l.music[i].musicName << RESETFMT << endl;
            continue;
        }
        cout << setfill(' ') << setw(3) << i << ": " << l.music[i].musicName << endl;
    }
}