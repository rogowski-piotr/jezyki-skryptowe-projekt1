#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <chrono>
#include "function.h"
#include "utils.h"

using namespace std;

string DATASET_PATH = "dataset.txt";
int DATASET_SIZE = 2000;
long long int REPETITIONS = 300000;
string OUTPUT_PATH = "result_cpp.txt";

int main() {
    
    /*******************************
    *       READING DATASET        *
    ********************************/
    ifstream stream_dataset(DATASET_PATH);
    string line;
    int line_number = 0;

    string characters_array[DATASET_SIZE];
    string excluded_array[DATASET_SIZE];

    while (getline (stream_dataset, line)) {
        line_number++;
        int dataset_index = line_number % 2 ? line_number / 2 : line_number / 2 - 1;
        string converted_line = convert_str_ascii_to_string(line);

        if (line_number % 2) characters_array[dataset_index] = converted_line;
        else excluded_array[dataset_index] = converted_line;
    }

    stream_dataset.close();


    /*******************************
    *   PERFORMANCE MEASUREMENT    *
    ********************************/
   
   /*for (int dataset_index = 0; dataset_index < DATASET_SIZE; dataset_index++) {
        string characters = characters_array[dataset_index];
        string excluded = excluded_array[dataset_index];
        string str = excluded.size() ? function(characters, excluded) : function(characters);
        cout << "characters: " << characters.size() << ";\t: " << characters << endl;
        cout << "excluded: " << excluded.size() << ";\t: " << excluded << endl;
        cout << "result: " << str.size() << ";\t: " << str << endl << endl;
        result[dataset_index] = str;
    }*/
    
    auto t0 = chrono::steady_clock::now();
    for (int r = 0; r < REPETITIONS; r++) {
        for (int dataset_index = 0; dataset_index < DATASET_SIZE; dataset_index++) {
            if (excluded_array[dataset_index].size()) { } else { }
        }
    }

    auto t1 = chrono::steady_clock::now();
    for (int r = 0; r < REPETITIONS; r++) {
        for (int dataset_index = 0; dataset_index < DATASET_SIZE; dataset_index++) {
            if (excluded_array[dataset_index].size()){
               function(characters_array[dataset_index], excluded_array[dataset_index]);
            } else {
                function(characters_array[dataset_index]);
            }
        }
    }
    auto t2 = chrono::steady_clock::now();
 
    int empty_loop = chrono::duration_cast<chrono::seconds>(t1 - t0).count();
    int loop = chrono::duration_cast<chrono::seconds>(t2 - t1 ).count();
    printf("%d [s] -> empty loop\n", empty_loop);
    printf("%d [s] -> empty loop + calculations\n", loop);
    printf("%d [s] -> pure calculations \n", loop - empty_loop);

    /*******************************
    *          SAVE RESULT         *
    ********************************/
    string result[DATASET_SIZE];
    for (int dataset_index = 0; dataset_index < DATASET_SIZE; dataset_index++) {
        string str = excluded_array[dataset_index].size() ? function(characters_array[dataset_index], excluded_array[dataset_index]) : function(characters_array[dataset_index]);
        result[dataset_index] = str;
    }

    ofstream stream_output(OUTPUT_PATH);
    for (int i = 0; i < DATASET_SIZE; i++) {
        stream_output << result[i] << endl;
    }
    stream_output.close();

    return 0;
}