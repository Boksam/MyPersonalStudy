#include <iostream>
#include <map>
#include <regex>
#include <cctype>
using namespace std;
int main() {
    string str,c;
    map<string, int> words;
    int i = 0;
    while (cin >> str && str!="^") {
        auto filtered = regex_replace(str, regex("[.|,|:|;| ]"), "");
        transform(filtered.begin(), filtered.end(), filtered.begin(), ::tolower);

        auto search = words.find(filtered);
        if (search != words.end()) {
            words[filtered]++;
        }
        else {
            words.insert(make_pair(filtered, 1));
        }
    }

    cout << "words: " << words.size() << endl;

    while(cin>>c){
        if(c=="QUIT"){
            cout<<"Bye!" << endl;
            break;
        }
        cout<< c << ": " << words[c] << endl;
    }
}