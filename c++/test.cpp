#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    vector<string> temp;
    temp.push_back("Hello");
    temp.push_back("C++");
    
    for (auto it : temp){
        cout << it << endl;
    }
    return 0;
}