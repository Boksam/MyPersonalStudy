#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

struct info{
    int level = 0;
    string supMember = "";
    set<string> subMember;      // set을 이용해 부하가 중복되지 않도록 설정
};

map<string, info> memberList;

int N;


void input(){
    for (int i = 1; i < N; i++){
        string under, top;
        cin >> under >> top;

        info supInfo, subInfo;

        if (memberList.find(under) != memberList.end()){     // when under exist already
            memberList[under].supMember = top;
        }
        else{                                                // when under doesn't exist
            subInfo.supMember = top;
            memberList.insert(make_pair(under, subInfo));
        }

        if (memberList.find(top) == memberList.end()){      // when top doesn't exist
            memberList.insert(make_pair(top, supInfo));
        }
    }
}

void getAllLevelandSubMember(){      // 모든 노드의 root로부터의 거리와 자신을 상위 멤버의 부하로 추가하는 함수
    for (auto &it : memberList){
        int tempLevel = 0;
        string tempNode = it.first;

        while(memberList[tempNode].supMember != ""){
            tempLevel++;

            tempNode = memberList[tempNode].supMember;
            memberList[tempNode].subMember.insert(it.first);
        }
        it.second.level = tempLevel;
    }
}

bool cmp(pair<string, info> &p1, pair<string, info> &p2){
    if (p1.second.subMember.size() > p2.second.subMember.size())    // 부하 수 비교
        return true;
    if (p1.second.subMember.size() < p2.second.subMember.size())
        return false;

    if (p1.second.level > p2.second.level)      // Root로부터 거리 비교
        return false;
    if (p1.second.level < p2.second.level)
        return true;

    if (p1.first > p2.first)        // 이름 비교
        return false;
    if (p1.first < p2.first)
        return true;
}

int main(){
    cin >> N;

    input();
    
    getAllLevelandSubMember();


    vector< pair<string, info> > vec(memberList.begin(), memberList.end()); // sort를 위해 map을 vector로 옮기기

    sort(vec.begin(), vec.end(), cmp);

    for (auto it : vec){
        cout << it.first << '\n';
    }

    return 0;
}