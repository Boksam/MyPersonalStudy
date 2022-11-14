#include <iostream>
#include <stack>
using namespace std;

int current_complexity = 0;
int total_complexity = 0;


int main(){
    char inputChar;
    while(cin >> inputChar){
        if (inputChar == '{'){
            total_complexity += ++current_complexity;
        }
        else if (inputChar == '}'){
            current_complexity--;
        }
    }

    cout << total_complexity << endl;
    return 0;
}