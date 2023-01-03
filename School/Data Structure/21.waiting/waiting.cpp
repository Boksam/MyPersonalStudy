#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

class Guest {
    int enterTime;
    int id;
    int remainingTime;
public:
    Guest(int _enterTime, int _id, int _remainingTime) :
        enterTime(_enterTime), id(_id), remainingTime(_remainingTime) {}
    
    int getEnterTime() const { return enterTime; }

    int getRemainingTime() const { return remainingTime; }
    int setRemainingTime(int _remainingTime) { remainingTime = _remainingTime; }

    int getId() const { return id; }

    bool operator < (const Guest& other) const {        // priority_queue 정렬
        if (remainingTime < other.getRemainingTime())
            return true;
        else if (remainingTime == other.getRemainingTime())
            return id > other.getId();
        else
            return false;
    }

    int consulting() {
        int consultingTime;
        if (remainingTime <= 10){
            consultingTime = remainingTime;
            remainingTime = 0;
        }
        else {
            consultingTime = remainingTime / 2;
            remainingTime -= consultingTime;
        }
        return consultingTime;
    }
};


bool cmpEnterTime (Guest &a, Guest& b){
    return a.getEnterTime() > b.getEnterTime();
}


int main(){
    int N; cin >> N;

    vector<Guest> guestList;
    priority_queue<Guest> waitRoom;
    vector<int> outID;

    for (int i = 0; i < N; i++) {       // 게스트 일단 다 저장하자~~
        int tmpEnterTime, tmpID, tmpRemainingTime;
        cin >> tmpEnterTime >> tmpID >> tmpRemainingTime;

        guestList.push_back(Guest(tmpEnterTime, tmpID, tmpRemainingTime));
    }

    sort(guestList.begin(), guestList.end(), cmpEnterTime);

    int time = 30;      // 시간 변수 만들어보자~~
    
    while (!guestList.empty() || !waitRoom.empty()) {       // 한번 상담 해보자~~
        while (!guestList.empty() && guestList.back().getEnterTime() <= time) {
            waitRoom.push(guestList.back());
            guestList.pop_back();
        }

        if (waitRoom.empty()) {     // 손님이 없으면 다음 손님 올때까지 기다리자~~
            time = guestList.back().getEnterTime();
            continue;
        }

        Guest guest = waitRoom.top();
        waitRoom.pop();

        time += guest.consulting();         // 상담 시간만큼 시간 추가해보자~~

        if (guest.getRemainingTime() != 0)
            waitRoom.push(guest);
        else{
            outID.push_back(guest.getId());
        }
    }

    for (auto it : outID)
        cout << it << '\n';

    return 0;
}