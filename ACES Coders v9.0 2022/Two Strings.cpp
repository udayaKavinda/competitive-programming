#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, m;
    string s1, s2;
    cin >> n >> s1 >> m >> s2;

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (s2.find(s1[i]) != string::npos) {
            count++;
            s2.erase(s2.find(s1[i]), 1);
        }
    }

    cout << count << endl;
    return 0;
}
