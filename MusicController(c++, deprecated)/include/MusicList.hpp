//
// Created by Charlie on 2020/10/10.
//

#include <string>

#include "Format.hpp"
#include "Strs.hpp"

#ifndef MUSICCONTROLLER_MUSICLIST_HPP
#define MUSICCONTROLLER_MUSICLIST_HPP

using namespace std;
namespace fs = std::__fs::filesystem;

typedef struct NodeMusic
{
    string musicName;
} NodeMusic;

typedef struct MusicListRep {
    vector<NodeMusic>   music;
    int                 curr{};
} MusicList;


/** FUNCTIONS **/

/**
 * Create a new MusicList.
 * @return MusicList
 */
MusicList newMusicList();

/**
 * Add a music to MusicList. If this music exists, then it will not be added.
 * @return 1 if success, or 0 if fail.
 */
int addMusic(MusicList&, const string&);

/**
 * Load music from a directory.
 */
void loadMusic(MusicList&, const char *);


/**
 * Check if the music exists in MusicList.
 * @return {@code true} if it exists, or {@code false} if not.
 */
bool musicExist(MusicList, const string&);

/**
 * Find the index of a specific music.
 * @return the index of that music
 */
int musicIndex(MusicList, const string&);

/**
 * Set the current index to a specific value.
 */
void setCurrIndex(MusicList&, int);


int getCurrIndex(const MusicList&);
int getListSize(const MusicList&);
string getCurrMusic(MusicList);
void showAllMusic(MusicList);

NodeMusic newNodeMusic(const string&);


#endif //MUSICCONTROLLER_MUSICLIST_H
