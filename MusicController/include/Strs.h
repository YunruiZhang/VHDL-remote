//
// Created by Charlie on 2020/10/12.
//

#ifndef MUSICCONTROLLER_STRS_H
#define MUSICCONTROLLER_STRS_H

#include <string>
#include <iostream>
#include <vector>
using namespace std;

/**
 * Check if a string is ending with a substring.
 * @param fullString the initial string
 * @param ending the substring
 * @return {@code true} if {@code fullstring} ends with {@code ending}, or {@code false} if not
 */
static bool hasEnding(const string &fullString, const string &ending);

/**
 * Split a string to a vector.
 * @param str initial string
 * @param delim deliminator
 * @return a vector contains each substring
 */
static vector<string> split(const string& str, const string& delim);


static bool hasEnding(const string &fullString, const string &ending)
{
    if (fullString.length() >= ending.length())
    {
        return (0 == fullString.compare(fullString.length() - ending.length(), ending.length(), ending));
    }
    else
    {
        return false;
    }
}

static vector<string> split(const string& str, const string& delim)
{
    vector<string> res;
    if(str.empty()) return res;
    char * strs = new char[str.length() + 1] ;
    strcpy(strs, str.c_str());

    char * d = new char[delim.length() + 1];
    strcpy(d, delim.c_str());

    char *p = strtok(strs, d);
    while(p) {
        string s = p;
        if (hasEnding(s, "\n"))
        {
            s.assign(s,0,s.size()-1);
        }
        res.push_back(s);
        p = strtok(nullptr, d);
    }

    return res;
}

#endif //MUSICCONTROLLER_STRS_H
