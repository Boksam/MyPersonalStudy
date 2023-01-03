#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int imageSize, patternSize;
vector<string> image;
vector< pair<int, int> > answers;


void inputImage() {
    ifstream inputFile;
    inputFile.open("map.txt");

    inputFile >> imageSize;

    string tempStr;
    getline(inputFile, tempStr);
    while (getline(inputFile, tempStr)) {
        image.push_back(tempStr);
    }

    inputFile.close();
}


void check(string &patternString) {
    for (int i = 0; i <= imageSize - patternSize; i++) {
        for (int j = 0; j <= imageSize - patternSize; j++) {
            
            string testPattern;
            for (int k = 0; k < patternSize; k++) {
                testPattern += image[i + k].substr(j, patternSize);
            }
        
            if (testPattern.compare(patternString) == 0)
                answers.push_back(make_pair(j + 1, i + 1));
        }
    }
}

int main() {

    inputImage();
    
    cin >> patternSize;

    string patternString;
    for (int i = 0; i < patternSize; i++) {
        string temp;
        cin >> temp;
        patternString += temp;
    }

    check(patternString);

    if (answers.size() == 0) {
        cout << "0 0\n";
    }
    else {
        for (auto it : answers)
            cout << it.first << " " << it.second << '\n';
    }
}