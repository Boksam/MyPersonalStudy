#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    vector<string> pList;
    pList.push_back("ddd");
    pList.push_back("eee");
    pList.push_back("zzz");
    pList.push_back("aaa");
    pList.push_back("bbb");
    sort(pList.begin(), pList.end());
    
    for (auto it : pList)
        cout << it << " ";
    cout << '\n';
}