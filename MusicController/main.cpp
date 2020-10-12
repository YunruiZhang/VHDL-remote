//
// Created by Charlie on 2020/10/13.
//

#include <Command.h>
#include <Controller.h>
#include <Format.h>

int main (void)
{
    auto * c = new Controller();

    cout << endl << BLUE << "WELCOME!" << endl;

    char cmd[256];

    printPrompt();

    while (fgets(cmd, 256, stdin) != nullptr)
    {
        handleCommand(c, cmd);
        printPrompt();
    }

    return 0;
}