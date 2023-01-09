#include <iostream>
#include <queue>
using namespace std;

priority_queue<int> pq;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N;
    cin >> N;

    for (int i =0; i < N; i++) {
        int val;
        cin >> val;

        if (val == 0) {
            if (pq.empty()) cout << "0\n";
            else {
                cout << pq.top() << '\n';
                pq.pop();
            }
        }
        else {
            pq.push(val);
        }
    }
    return 0;
}