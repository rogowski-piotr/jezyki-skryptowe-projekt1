#include <iostream>
#include <fstream>
#include <string>
#include "function.h"

using namespace std;

int main() {
    // cout << "Starting" << endl;

    // string to_strip = "\ta\tbc\ta\taa";
    // string str = function(to_strip, "a\t");
    // cout << to_strip << endl;
    // cout << str << endl;

    string FILE_PATH = "dataset.txt";
    ifstream stream(FILE_PATH);
    string line;
    int line_number = 0;

    string characters_array[3];
    string excluded_array[3];

    while (getline (stream, line)) {
        line_number++;
        if (line_number % 2) {
            cout << line_number << " to characters_array " << line << endl;
            cout << "index: " << (line_number % 2 ? line_number / 2 : line_number / 2 - 1) << endl;
            characters_array[line_number % 2 ? line_number / 2 : line_number / 2 - 1] = line;
        } else {
            cout << line_number << " to excluded_array " << line << endl;
            cout << "index: " << (line_number % 2 ? line_number / 2 : line_number / 2 - 1) << endl;
            excluded_array[line_number % 2 ? line_number / 2 : line_number / 2 - 1] = line;
        }
    }

    
    stream.close();

    for (int i = 0; i < 3; i++) {
        cout << characters_array[i] << endl;
        cout << excluded_array[i] << endl;
    }

    

    return 0;
}