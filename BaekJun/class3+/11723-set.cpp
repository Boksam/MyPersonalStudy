#include <iostream>
#include <set>
using namespace std;

set <int> s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int M;
    cin >> M;

    string query;
    int value;
    for (int i =0; i < M; i++) {
        cin >> query;
        if (query == "all") {
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
            continue;
        }
        else if (query == "empty") {
            s.clear();
            continue;
        }

        cin >> value;

        if (query == "add") {
            s.insert(value);
        }
        else if (query == "remove") {
            s.erase(value);
        }
        else if (query == "check") {
            if (s.find(value) != s.end())
                cout << "1\n";
            else
                cout << "0\n";
        }
        else if (query == "toggle") {
            if (s.find(value) != s.end())
                s.erase(value);
            else
                s.insert(value);
        }
    }

    return 0;
}