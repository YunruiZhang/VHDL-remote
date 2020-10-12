//
// Created by Charlie on 2020/10/10.
//

#include <algorithm>
#include <cstdlib>
#include <dirent.h>
#include <Format.h>
#include "MusicList.h"

/**
 * Check if a file is playable by its suffix.
 * @return {@code true} if suffix matches any video or music format, or {@code false} if none
 */
static bool isPlayable(const char *);

struct MusicListRep {
    ItemMusic **music;
    int         size;
    int         curr;
};

MusicList newMusicList()
{
    auto l = static_cast<MusicList>(malloc(sizeof(struct MusicListRep)));
    l->music = static_cast<ItemMusic **>(malloc(sizeof(ItemMusic *)));
    l->music[0] = static_cast<ItemMusic *>(malloc(sizeof(ItemMusic)));
    l->size = 0;
    l->curr = 0;
    return l;
}

void addMusic(MusicList l, const char *name)
{

    if (!musicExist(l, name) && isPlayable(name))
    {
        if (l->size == 0)
        {
            strcpy(l->music[0]->musicName, name);
        }
        else
        {
            l->music = static_cast<ItemMusic **>(realloc(l->music, (++l->size) * sizeof(ItemMusic)));
            strcpy(l->music[l->size - 1]->musicName, name);
        }
    }
}

void loadMusic(MusicList l, const char *dir)
{
    DIR * d;
    struct dirent *ent;
    if ((d = opendir(dir)) != nullptr)
    {
        while ((ent = readdir(d)) != nullptr)
        {
            addMusic(l, ent->d_name);
        }
    }
    else
    {
        PrintError("Failed to open directory: " << dir);
        return;
    }
    PrintSuccess("Currently " << l->size << " songs.");
}

bool musicExist(MusicList l, const char * name)
{
    return musicIndex(l, name) != -1;
}

void freeMusicList(MusicList l)
{
    for (int i = 0; i < l->size; i++)
    {
        free(l->music[i]);
    }
    free(l->music);
    free(l);
}

int musicIndex(MusicList l, const char * name)
{
    for (int i = 0; i < l->size; i++)
    {
        if (l->music[i]->musicName == name)
        {
            return i;
        }
    }
    return -1;
}

void setCurrIndex(MusicList l, int x)
{
    l->curr = x;
}

static bool isPlayable(const char * name)
{
    string audioFormat[] = {".mp3", ".wav", ".wma", ".m4a", ".aac"};

    for (const auto & i : audioFormat)
    {
        if (hasEnding(name, i)) return true;
    }
    
    return false;
}

int getCurrIndex(MusicList l)
{
    return l->curr;
}

int getListSize(MusicList l)
{
    return l->size;
}

char * getCurrentMusic(MusicList l)
{
    return l->music[l->curr]->musicName;
}