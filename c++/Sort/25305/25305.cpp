#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main() {
	int N, k;
	cin >> N >> k;

	vector<int> v(N);
	for (int i = 0; i < N; i++) {
		cin >> v[i];
	}
	sort(v.begin(), v.end());

	cout << *(v.end() - k);
	return 0;
}