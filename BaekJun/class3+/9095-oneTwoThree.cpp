#include <iostream>
using namespace std;

int num[12];

int main() {
    num[0] = 1;
    num[1] = 1;
    num[2] = 2;

    for (int i = 3; i < 12; i++) {
        num[i] = num[i-3] + num[i-2] + num[i-1];
    }
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int query;
        cin >> query;

        cout << num[query] << '\n';
    }
}  