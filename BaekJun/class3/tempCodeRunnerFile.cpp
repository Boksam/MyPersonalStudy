#include <iostream>
#include <vector>
using namespace std;

bool isBroken[10] = { false, };
int N, M, optimalNum = 10000000, minDiff = 99999900;


bool check(int num) {
    while (num != 0) {
        if (isBroken[num % 10])
            return false;
        num /= 10;
    }
    return true;
}


int main() {
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int temp;
        cin >> temp;
        isBroken[temp] = true;
    }

    for (int i = 0; i < 1000001; i++) {
        if (check(i)) {
            int newDiff = abs(i - N);
            if (newDiff < minDiff) {
                minDiff = newDiff;
                optimalNum = i;
            }
        }
    }

    int digit = 0, tempOptimalNum = optimalNum;
    while (tempOptimalNum != 0) {
        digit++;
        tempOptimalNum /= 10;
    }

    int answer = min(abs(N - 100), digit + minDiff);
    cout << answer << endl;
}