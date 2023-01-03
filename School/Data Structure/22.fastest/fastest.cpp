#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define INF 1e9

int n, m, start;

vector< pair<char, int> >graph[26]; // alphabet to num, first : name, second : cost
int d[26];
int dimensions[26];

int dijkstra(int start) {
    priority_queue< pair<int, int> >pq; // first : cost, second : name
    pq.push(make_pair(0, start));
    d[start] = 0;

    while(!pq.empty()) {
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (d[now] < dist)
            continue;
        
        for (int i = 0; i < graph[now].size(); i++) {
            int cost = dist + graph[now][i].second * 2;
            if (now != start)
                cost += dimensions[now];

            if (cost < d[graph[now][i].first]) {
                d[graph[now][i].first] = cost;
                pq.push(make_pair(-cost, graph[now][i].first));
            }
        }
    }
    
    int maxDiameter = 0;
    for (int i = 0; i < 26; i++) {
        if (d[i] == INF)
            continue;
        maxDiameter = max(maxDiameter, d[i]);
    }
    return maxDiameter;
}


int main(){
    int N;
    cin >> N;
    for (int i = 0; i < N; i++){
        char alphaStartP, alphaEndP;
        int distance, dimension = 0;
        
        cin >> alphaStartP;
        int startP = alphaStartP - 'A';
        while (cin >> alphaEndP) {
            if (alphaEndP == '$')
                break;
            int endP = alphaEndP - 'A';
            cin >> distance;
            graph[startP].push_back(make_pair(endP, distance));
            dimension++;
        }
        dimensions[startP] = dimension;
    }


    int maxDiameter = -1;
    for (int i = 0; i < N; i++) {
        if (graph[i].empty())
            continue;
        fill(d, d + 26, INF);
        int newDiameter = dijkstra(i);
        maxDiameter = max(newDiameter, maxDiameter);
    }

    cout << maxDiameter << endl;
    return 0;
}