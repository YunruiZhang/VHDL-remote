//
// Created by Charlie on 2020/10/13.
//

#include <Command.h>

void helpCommand()
{
    cout <<
    "    help             To see all the commands you can type" << endl <<
    "    load <dir>       Load music from directory dir" << endl <<
    "    play             Play" << endl <<
    "    stop             Stop" << endl <<
    "    pause            Pause" << endl <<
    "    prev             Previous song" << endl <<
    "    next             Next song" << endl <<
    "    volume [id]      Increase(i) or decrease(d) volume." << endl <<
    "    mode [ors]       Play music orderly(o), randomly(r) or circularly(s)" << endl <<
    "    quit             Quit the program" << endl;
}

void handleCommand(Controller * c, const char * cmdin)
{
    vector<string> cmd = split(cmdin, " ");

    if (cmd[0] == "help")
    {
        helpCommand();
    }
    else if (cmd[0] == "load")
    {
        if (cmd.size() < 2)
        {
            PrintError("You must specify a directory.");
            return;
        }

        c->loadMusicFromDir(cmd[1].c_str());
    }
    else if (cmd[0] == "play")
    {
        c->play();
        PrintSuccess("Played");
    }
    else if (cmd[0] == "pause")
    {
        c->pause();
        PrintSuccess("Paused.");
    }
    else if (cmd[0] == "stop")
    {
        c->stop();
        PrintSuccess("Stopped.");
    }
    else if (cmd[0] == "prev")
    {
        c->previous();
        PrintSuccess("Changed to the previous song.");
    }
    else if (cmd[0] == "next")
    {
        c->next();
        PrintSuccess("Changed to the next song.");
    }
    else if (cmd[0] == "volume")
    {
        if (cmd.size() < 2 || (cmd[1] != "i" && cmd[1] != "d"))
        {
            PrintError("You must specify i(ncrease) or d(ecrease).");
            return;
        }

        if (cmd[1] == "i")
        {
            c->volumeUp();
            PrintSuccess("Volume increased.");
        }
        else if (cmd[1] == "d")
        {
            c->volumeDown();
            PrintSuccess("Volume deceased.");
        }
    }
    else if (cmd[0] == "mode")
    {
        if (cmd.size() < 2 || (cmd[1] != "r" && cmd[1] != "s" && cmd[1] != "o"))
        {
            PrintError("You must specify the order in o(rderly), s(ingle song) or r(andomly).");
            return;
        }

        if (cmd[1] == "r")
        {
            c->setMode(RANDOM_PLAY);
            PrintSuccess("Music will be played randomly.");
        }
        else if (cmd[1] == "s")
        {
            c->setMode(SINGLE_PLAY);
            PrintSuccess("Music will be played circularly.");
        }
        else if (cmd[1] == "o")
        {
            c->setMode(ORDER_PLAY);
            PrintSuccess("Music will be played orderly.");
        }
    }
    else if (cmd[0] == "quit")
    {
        cout << GREEN << "Quitting..." << RESETFMT << endl << endl;
        exit(EXIT_SUCCESS);
    }
    else if (cmd[0].empty())
    {
        return;
    }
    else
    {
        cout << ERRORINFO << "Cannot cast " << BOLD << cmd[0] << RESETFMT << " into any command."
                                                                             " You may type \"help\"." << endl;
    }
}

void printPrompt()
{
    cout << "\n" << YELLOW << "Command: " << RESETFMT;

}

