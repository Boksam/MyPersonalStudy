#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int k;  // size is 2^k
string token;   // query token
vector<char> total_qts; // to save qts
vector< vector<char> > total_img;   // to save img

int QtsToImg(int size, int idx, int y, int x){
    char curr_qts = total_qts[idx];
    if (curr_qts == '('){
        idx = QtsToImg(size / 2, idx + 1, y, x + size / 2);
        idx = QtsToImg(size / 2, idx + 1, y, x);
        idx = QtsToImg(size / 2, idx + 1, y + size /2, x);
        idx = QtsToImg(size / 2, idx + 1, y + size / 2, x + size / 2);
        return idx + 1;     // next element is ')' so pass
    }
    else{
        for (int i = y; i < y + size; i++)
            for (int j = x; j < x + size; j++)
               total_img[i][j] = curr_qts;
        return idx;
    }
}

void ImgToQts(int size, int y, int x){
    char curr_block = total_img[y][x];

    for (int i = y; i < y + size; i++)
        for (int j = x; j < x + size; j++)
            if (total_img[i][j] != curr_block){
                total_qts.push_back('(');
                ImgToQts(size / 2, y, x + size / 2);
                ImgToQts(size / 2, y, x);
                ImgToQts(size / 2, y + size / 2, x);
                ImgToQts(size / 2, y + size / 2, x + size / 2);
                total_qts.push_back(')');
                return;
            }
    total_qts.push_back(curr_block);
}

int main(){
    cin >> k >> token;
    int img_size = 1;
    for (int i = 0; i < k; i++) img_size *= 2;
    total_img.resize(img_size, vector<char>(img_size));

    if (token == "QTS"){    // QTS query
        string qts;
        cin >> qts;
        for (char &c : qts)
            total_qts.push_back(c);
        
    QtsToImg(img_size, 0, 0, 0);    // size, idx, y, x
    for (auto y : total_img){
        for (char& x : y)
            cout << x;
        cout << '\n';
    }
    }
    else{       // IMG query
        for (int i = 0; i < img_size; i++)
            for (int j = 0; j < img_size; j++)
                cin >> total_img[i][j];
        
        ImgToQts(img_size, 0, 0);   // size, y, x
        for (char it : total_qts)
            cout << it;
        cout << '\n';
    }
}