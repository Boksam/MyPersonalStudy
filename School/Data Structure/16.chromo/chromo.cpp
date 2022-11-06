#include <iostream>
#include <list>
#include <algorithm>
#include <fstream>

#define list_iter list<char>::iterator

using namespace std;

list<char> genome;

bool checkRange(int i, int j){
    if (i >= genome.size() || j >= genome.size())
        return false;
    return true;
}

list_iter getIter(int idx){
    list_iter temp_iter = genome.begin();
    advance(temp_iter, idx);
    return temp_iter;
}

void getDataAndSave(){
    ifstream infile("sapiens.txt");
    
    string tempstr;
    getline(infile, tempstr);
    char temp;
    while(infile.get(temp)){
        if (temp != '\n' and temp != '\r')
            genome.push_back(temp);
    }
}

void _front(int i, int j){
    if (!checkRange(i, j))
        return;

    list_iter start_iter = getIter(i);
    list_iter end_iter = getIter(j + 1);
    
    genome.splice(genome.begin(), genome, start_iter, end_iter);
}

void _back(int i, int j){
    if (!checkRange(i, j))
        return;
    
    list_iter start_iter = getIter(i);
    list_iter end_iter = getIter(j + 1);

    genome.splice(genome.end(), genome, start_iter, end_iter);
}

void _cut(int i, int j){
    if (!checkRange(i, j))
        return;
    
    list_iter start_iter = getIter(i);
    list_iter end_iter = getIter(j + 1);

    list<char> tempList;
    tempList.splice(tempList.begin(), genome, start_iter, end_iter);
}

void _double(int i, int j){
    if (!checkRange(i, j))
        return;
    
    list_iter start_iter = getIter(i);
    list_iter end_iter = getIter(j + 1);

    list<char> tempList;
    list_iter temp_iter = start_iter;
    while(temp_iter != end_iter)
        tempList.push_back(*temp_iter++);

    genome.splice(end_iter, tempList, tempList.begin(), tempList.end());
}

void _flip(int i, int j){
    if (!checkRange(i, j))
        return;
    
    list_iter start_iter = getIter(i);
    list_iter end_iter = getIter(j + 1);

    reverse(start_iter, end_iter);
}

void _report(int i, int j){
    if (i > genome.size()){
            cout << "NONE\n";
            return;
    }
    if (j > genome.size())
        j = genome.size() - 1;

    list_iter start_iter = getIter(i);
    list_iter end_iter = getIter(j + 1);

    while (start_iter != end_iter)
        cout << *start_iter++;
    cout << endl;
}

int main(){
    getDataAndSave();
    
    int N;
    cin >> N;

    for(int i = 0; i < N; i++){
        int startIdx, endIdx;
        string query;
        cin >> query >> startIdx >> endIdx;
        startIdx--;
        endIdx--;

        
        
        if (query == "front")
            _front(startIdx, endIdx);
        else if (query == "back")
            _back(startIdx, endIdx);
        else if (query == "cut")
            _cut(startIdx, endIdx);
        else if (query == "double")
            _double(startIdx, endIdx);
        else if (query == "flip")
            _flip(startIdx, endIdx);
        else if (query == "report")
            _report(startIdx, endIdx);
    }

    return 0;
}