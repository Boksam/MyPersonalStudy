#include <iostream>
#include <list>
#include <algorithm>
using namespace std;


int main(){
    list<int> myList;
    for (int i = 0; i < 20; i++){
        myList.push_back(i);
    }
    int i = 10, j = 16;

    list<int>::iterator start_iter = myList.begin();
    list<int>::iterator end_iter = myList.begin();
    advance(start_iter, i);
    advance(end_iter, j);

    reverse(start_iter, end_iter);
    
    for (auto it : myList)
        cout << it << " ";
    cout << endl;
}