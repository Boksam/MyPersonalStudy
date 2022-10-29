#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define pii pair<int, int>
#define forDiskLoop for(int i = 0; i < disk.size(); i++)

vector< pair<string, pii> > disk;
int diskSize, remainSize;
string targetName;


bool comp(pair<string, pair<int, int> > &p){
    if (p.first == targetName)
        return true;
    return false;
}


bool findTarget(string name){
    if (find_if(disk.begin(), disk.end(), comp) == disk.end())
        return false;
    return true;
}

void _write(){
    string name;
    int fileSize;
    cin >> name >> fileSize;

    targetName = name;
    if (findTarget(name)){
        cout << "error\n";
        return;
    }

    if (remainSize < fileSize){
        cout << "diskfull" << '\n';
        return;
    }

    remainSize -= fileSize;     // 넣을 자리가 있으므로 미리 남은 용량 빼기

    if (disk.empty()){
        disk.push_back(make_pair(name, make_pair(0, fileSize)));
        return;
    }

    // 한 묶음 확인
    pii previous = make_pair(0,0);
    pii current = make_pair(0,0);
    forDiskLoop{
        current = disk[i].second;
        int gap = current.first - previous.second;
        if (gap >= fileSize){
            disk.insert(disk.begin() + i, make_pair(name, make_pair(previous.second, previous.second + fileSize)));
            return;
        }
        previous = disk[i].second;
    }
    if (diskSize - previous.second >= fileSize){
        disk.push_back(make_pair(name, make_pair(previous.second, previous.second + fileSize)));
        return;
    }

    // 나눠서 저장
    previous = make_pair(0,0);
    current = make_pair(0,0);
    forDiskLoop{
        current = disk[i].second;
        int gap = current.first - previous.second;
        if (gap >= fileSize){
            disk.insert(disk.begin() + i, make_pair(name, make_pair(previous.second, previous.second + fileSize)));
            return;
        }
        if (gap != 0){
            disk.insert(disk.begin() + i++, make_pair(name, make_pair(previous.second, current.first)));
            fileSize -= gap;
        }
        previous = disk[i].second;
    }
    disk.push_back(make_pair(name, make_pair(previous.second, previous.second + fileSize)));
}


void _show(){
    string name;
    cin >> name;

    targetName = name;
    if (!findTarget(name)){
        cout << "error\n";
        return;
    }

    for (auto it : disk){
        if (it.first == name)
            cout << it.second.first << " ";
    }
    cout << '\n';
}


void _delete(){
    string name;
    cin >> name;

    targetName = name;
    if (!findTarget(name)){
        cout << "error\n";
        return;
    }

    forDiskLoop{
        if (disk[i].first == name){
            remainSize += disk[i].second.second - disk[i].second.first;
            disk.erase(disk.begin() + i);
        }
    }
}


void _compact(){
    if (disk.empty())
        return;

    pii previous = make_pair(0,0);
    pii current = make_pair(0,0);
    forDiskLoop{
        current = disk[i].second;
        int gap = current.first - previous.second;
        if (gap > 0){
            disk[i].second.first -= gap;
            disk[i].second.second -= gap;

            if (i != 0 && disk[i-1].first == disk[i].first){
            disk[i-1].second.second = disk[i].second.second;
            disk.erase(disk.begin() + i--);
            }  
        }
        previous = disk[i].second;
    }
}

int main(){
    cin >> diskSize;
    remainSize = diskSize;

    while(true) {
        string query;
        cin >> query;
        
        if (query == "end")
            break;

        if (query == "write")
            _write();
        
        if (query == "show")
            _show();

        if (query == "delete")
            _delete();

        if (query == "compact")
            _compact();
    }

    return 0;
}