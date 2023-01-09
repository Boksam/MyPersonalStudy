#include <iostream>
#include <queue>
#include <map>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        priority_queue<int, vector<int>, greater<int>> minPQ;
        priority_queue<int, vector<int>, less<int>> maxPQ;
        map<int, int> myMap;
        int operationSize;
        cin >> operationSize;

        for (int j = 0; j < operationSize; j++) {
            string operation; int value;
            cin >> operation >> value;

            if (operation == "I") {
                minPQ.push(value);
                maxPQ.push(value);
                myMap[value]++;
            }
            else {
                if (value == -1) {
                    while (!minPQ.empty() && myMap[minPQ.top()] == 0)
                        minPQ.pop();

                    if (!minPQ.empty()) {
                        myMap[minPQ.top()]--;
                        minPQ.pop();
                    }
                }
                if (value == 1) {
                    while (!maxPQ.empty() && myMap[maxPQ.top()] == 0)
                        maxPQ.pop();

                    if (!maxPQ.empty()) {
                        myMap[maxPQ.top()]--;
                        maxPQ.pop();
                    }
                }
            }
        }
        while (!minPQ.empty() && myMap[minPQ.top()] == 0)
            minPQ.pop();
        while (!maxPQ.empty() && myMap[maxPQ.top()] == 0)
            maxPQ.pop();

        if (minPQ.empty() && maxPQ.empty()) cout << "EMPTY\n";
        else cout << maxPQ.top() << " " << minPQ.top() << '\n';
    }
}
