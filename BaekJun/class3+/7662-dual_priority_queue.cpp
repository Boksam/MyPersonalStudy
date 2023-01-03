#include <iostream>
#include <queue>
#include <vector>
#include <map>
using namespace std;

priority_queue<int, vector<int>, greater<int>> minPQ;
priority_queue<int, vector<int>, less<int>> maxPQ;
map<int, int> isPopped;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    string query;
    int value;
    for (int i = 0; i < T; i++) {
        int K, q_size = 0;
        cin >> K;
        for (int j = 0; j < K; j++) {
            cin >> query >> value;
            if (query == "I") {
                minPQ.push(value);
                maxPQ.push(value);
                isPopped[value] = 0;
                q_size++;
            }
            else if (query == "D") {
                if (q_size != 0) {
                    q_size--;
                    if (value == -1) {
                        while (isPopped[minPQ.top()] != 0) {
                            isPopped[minPQ.top()]--;
                            minPQ.pop();
                        }
                        isPopped[minPQ.top()]++;
                        minPQ.pop();
                    }
                    else if (value == 1) {
                        while (isPopped[maxPQ.top()] != 0) {
                            isPopped[maxPQ.top()]--;
                            maxPQ.pop();
                        }
                        isPopped[maxPQ.top()]++;
                        maxPQ.pop();
                    }
                }
            }
        }
        if (q_size == 0) cout << "EMPTY\n";
        else cout << maxPQ.top() << " " << minPQ.top() << '\n';

        while (!minPQ.empty()) minPQ.pop();
        while (!maxPQ.empty()) maxPQ.pop();
        isPopped.clear();
    }
}