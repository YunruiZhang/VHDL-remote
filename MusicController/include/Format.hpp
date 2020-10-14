//
// Created by Charlie on 2020/10/12.
//

#ifndef MUSICCONTROLLER_FORMAT_HPP
#define MUSICCONTROLLER_FORMAT_HPP

#define RESETFMT "\033[0m"

#define BOLD     "\033[1m"
#define INVERSE  "\033[7m"

#define RED      "\033[31m"
#define GREEN    "\033[32m"
#define YELLOW   "\033[33m"
#define BLUE     "\033[34m"

#define ERRORINFO           "\033[31mError: \033[0m"
#define SUCCESSINFO         "\033[32mSuccess: \033[0m"
#define PrintError(msg)     cout << ERRORINFO << msg << endl;
#define PrintSuccess(msg)   cout << SUCCESSINFO << msg << endl;


#endif //MUSICCONTROLLER_FORMAT_H
