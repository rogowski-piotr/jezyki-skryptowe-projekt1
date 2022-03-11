#include <iostream>
#include <string>
#include "function.h"

using namespace std;

string function(string characters, string exclude_characters) {
    int cut_head = 0, cut_tail = 0;
    
    for (int index = 0; index < characters.size(); index++) {
        bool found_in_excluded = false;
        for (int i = 0; i < exclude_characters.size(); i++) {
            if (characters[index] == exclude_characters[i]) {
                cut_head++;
                found_in_excluded = true;
                break;
            }
        }
        if (!found_in_excluded) break;
    }

    for (int index = characters.size() - 1; index >= 0; index--) {
        bool found_in_excluded = false;
        for (int i = 0; i < exclude_characters.size(); i++) {
            if (characters[index] == exclude_characters[i]) {
                cut_tail++;
                found_in_excluded = true;
                break;
            }
        }
        if (!found_in_excluded) break;
    }

    return characters.substr(cut_head, characters.size() - cut_tail - cut_head);
}
