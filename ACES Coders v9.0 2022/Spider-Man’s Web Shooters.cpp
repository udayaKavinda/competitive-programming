#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int num;
    cin >> num;
    vector<int> array(num);

    for (int i = 0; i < num; i++) {
        cin >> array[i];
    }

    sort(array.begin(), array.end());

    // Create a longarray with a size of 1e5+1, initialized with zeros
    vector<int> longarray(1000001, 0);

    for (int i = 0; i < num; i++) {
        longarray[array[i]] = 1;
    }
    int count=0;
    for (int i=1;i<100001;i++){
        for(int k=0;k<array.size()-1;k++){
            if (longarray[array[k]+i]==1){
                count++;
                break;
            }

        }
    }
    cout<<count;
    // Now, longarray contains 1s at positions corresponding to elements in 'array'

    return 0;
}
