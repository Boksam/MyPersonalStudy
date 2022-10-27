#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define pii pair<int, int>

vector< pair<string, pii> > disk;
int diskSize, remainSize;


void _write(){
    string name;
    int fileSize;
    cin >> name >> fileSize;

    if (remainSize < fileSize){
        cout << "diskfull" << '\n';
        return;
    }

    remainSize -= fileSize;     // 넣을 자리가 있으므로 미리 남은 용량 빼기

    if (disk.empty())
        disk.push_back(make_pair(name, make_pair(0, fileSize)));
    else{
        for (int i = 1; i < disk.size(); i++){
            int gap = disk[i].second.first - disk[i-1].second.second;
            if (gap != 0){
                if (fileSize > gap){
                    disk.insert(disk.begin() + i, make_pair(name, make_pair(disk[i-1].second.second, disk[i-1].second.second + gap)));
                    fileSize -= gap;
                }
                else{
                    disk.insert(disk.begin() + i, make_pair(name, make_pair(disk[i-1].second.second, disk[i-1].second.second + fileSize)));
                    return;
                }
            }
        }
        disk.push_back(make_pair(name, make_pair(disk.back().second.second, disk.back().second.second + fileSize)));
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
        
        /*if (query == "show")
            _show();

        if (query == "delete")
            _delete();

        if (query == "compact")
            _compact();*/
    }

    for (auto it : disk){
        cout << it.first << " [" << it.second.first << "," << it.second.second << "]\n";
    }

    return 0;
}