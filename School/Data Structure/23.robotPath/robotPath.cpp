#include <iostream>
#include <queue>
#include <iomanip>
using namespace std;

#define MAX_SIZE 15

int x_dir[4] = {1, 0, -1, 0};
int y_dir[4] = {0, -1, 0, 1};

class Block {
public:
    int x;
    int y;
    int cost;
    int dir;    // 0: right, 1: up, 2: left, 3: down

    Block(int _x, int _y, int _cost, int _dir)
    : x(_x), y(_y), cost(_cost), dir(_dir) {};

    Block() {
        x = -1;
        y = -1;
        cost = -1;
        dir = -1;
    }
};

int N, turnTime;
int maze[MAX_SIZE][MAX_SIZE];
bool visited[MAX_SIZE][MAX_SIZE] = { false, };
Block path[MAX_SIZE][MAX_SIZE];

queue<Block> q;

bool isValid(Block &b) {
    if (b.x >= 0 && b.x < N && b.y >= 0 && b.y < N)
        return true;
    else
        return false;
}

int bfs() {
    Block startBlock = Block(0, N-1, 0, -2);
    visited[N - 1][0] = true;
    q.push(startBlock);

    while (!q.empty()) {
        Block currBlock = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int newX = currBlock.x + x_dir[i];
            int newY = currBlock.y + y_dir[i];
            int newCost = currBlock.cost + 1;
            if (currBlock.dir != i && currBlock.dir != -2)
                newCost += turnTime;

            Block newBlock(newX, newY, newCost, i);

            // cout << "(" << currBlock.x << "," << currBlock.y << ") -> (" << newX << "," << newY << ")" << endl;
            // cout << "currBlock's cost, dir : " << currBlock.cost << ", " << currBlock.dir << endl;
            // cout << "newBlock's cost, dir : " << newBlock.cost << ", " << newBlock.dir << endl;
            
            if (isValid(newBlock) && maze[newY][newX] == 0) {
                if (!visited[newY][newX]) {
                    path[newY][newX] = newBlock;
                    visited[newY][newX] = true;
                    q.push(newBlock);
                }
                else if (path[newY][newX].cost >= newBlock.cost) {
                    path[newY][newX] = newBlock;
                    q.push(newBlock);
                }
            }
        }
    }
    if (path[0][N-1].cost == -1)
        return -1;
    else
        return path[0][N-1].cost;
}

int main() {
    cin >> N >> turnTime;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) 
            cin >> maze[i][j];
    
    int result = bfs();
    cout << result << endl;
    
    return 0;
}
