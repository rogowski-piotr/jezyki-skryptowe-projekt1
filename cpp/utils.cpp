#include <iostream>
#include <string>
#include "function.h"

using namespace std;

string convert_str_ascii_to_string(string ascii_string) {
    string chars = "";
    string single_ascii = "";

    for (int i = 0; i < ascii_string.size(); i++) {
        if (ascii_string[i] == 32) {
            chars += atoi(single_ascii.c_str());
            single_ascii = "";
        } else {
            single_ascii += ascii_string[i];
        }
    }
    return chars;
}