#include <iostream>
#include <set>
#include <sstream>
 
using namespace std;
 
int main() {
    int num;
    cin >> num; // Read the number of integers
    
    set<int> mySet;
    
    int numInt;
    for (int i = 0; i < num; ++i) {
        cin >> numInt; // Read each integer
        mySet.insert(numInt); // Insert each integer into the set
    }
    
    cout << mySet.size() << endl; // Print the number of distinct integers
 
    return 0;
