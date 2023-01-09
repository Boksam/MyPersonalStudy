#include <iostream>
#include <queue>
#include <vector>
using namespace std;

priority_queue<int, vector<int>, greater<int>> pq;

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int n;
        cin >> n;
        pq.push(n);
    }

    int time = 0, result = 0;
    while (!pq.empty()) {
        result += time + pq.top();
        time += pq.top();
        pq.pop();
    }

    cout << result << endl;
    return 0;
}
