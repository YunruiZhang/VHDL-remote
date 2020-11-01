//
// Created by Charlie on 2020/10/12.
//

#include <iostream>
#include <vector>

#include "Controller.hpp"
#include "Format.hpp"
#include "Strs.hpp"

#ifndef MUSICCONTROLLER_COMMAND_HPP
#define MUSICCONTROLLER_COMMAND_HPP

using namespace std;

void helpCommand();
void handleCommand(Controller *, const char *);
void printPrompt();

#endif //MUSICCONTROLLER_COMMAND_H
