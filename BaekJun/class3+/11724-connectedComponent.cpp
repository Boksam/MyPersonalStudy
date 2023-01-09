#include <iostream>
#include <stack>
#include <map>
#include <vector>
using namespace std;

bool checked[1001];
map<int, vector<int>> vertex;

int DFS() {
    int result = 0;

    for (auto mIt : vertex) {
        if (checked[mIt.first])
            continue;

        stack<int> myStack;
        myStack.push(mIt.first);

        while (!myStack.empty()) {
            int current = myStack.top();
            myStack.pop();

            if (checked[current])
                continue;
            else
                checked[current] = true;
            
            for (auto vIt : vertex[current]) {
                myStack.push(vIt);
            }
        }
        result++;
    }

    return result;
}

int main() {
    int N, M;
    cin >> N >> M;
    
    for (int i = 0; i < M; i++) {
        int p1, p2;
        cin >> p1 >> p2;
        vertex[p1].push_back(p2);
        vertex[p2].push_back(p1);
    }

    cout << DFS() << endl;
}