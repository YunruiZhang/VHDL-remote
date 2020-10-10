//
// Created by Charlie on 2020/10/10.
//
#include <string>
#ifndef MUSICCONTROLLER_MUSICLIST_H
#define MUSICCONTROLLER_MUSICLIST_H

using namespace std;

typedef struct ItemMusic
{
    char * musicName;
} ItemMusic;

typedef struct MusicListRep {
    ItemMusic **music;
    int         size;
    int         curr;
} * MusicList;


/** FUNCTIONS **/

/**
 * Create a new MusicList.
 * @return MusicList
 */
MusicList newMusicList();

/**
 * Add a music to MusicList. If this music exists, then it will not be added.
 */
void addMusic(MusicList, const char *);

/**
 * Load music from a directory.
 */
void loadMusic(MusicList, const char *);

/**
 * Free MusicList.
 */
void freeMusicList(MusicList);

/**
 * Check if the music exists in MusicList.
 * @return {@code true} if it exists, or {@code false} if not.
 */
bool musicExist(MusicList, const char *);

/**
 * Find the index of a specific music.
 * @return the index of that music
 */
int musicIndex(MusicList, const char *);

/**
 * Set the current index to a specific value.
 */
void setCurrIndex(MusicList, int);

#endif //MUSICCONTROLLER_MUSICLIST_H
