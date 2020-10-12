//
// Created by Charlie on 2020/10/12.
//

#include <iostream>
#include <Format.h>
#include <Strs.h>
#include <vector>
#include "Controller.h"
#ifndef MUSICCONTROLLER_COMMAND_H
#define MUSICCONTROLLER_COMMAND_H

using namespace std;

void helpCommand();
void handleCommand(Controller *, const char *);
void printPrompt();

#endif //MUSICCONTROLLER_COMMAND_H
