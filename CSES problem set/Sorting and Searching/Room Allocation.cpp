#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <tuple> // Include the tuple header
 
using namespace std;
 
int main() {
    int length;
    cin >> length;
    vector<pair<pair<int, int>, int>> arr;
 
    for (int i = 0; i < length; i++) {
        int x, y;
        cin >> x >> y;
        arr.push_back(make_pair(make_pair(x, y), i));
    }
 
    sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
        return a.first.first < b.first.first;
    });
 
    int count = 0;
    int roomNext = 1;
    vector<int> rooms(length, 0);
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> priorityQueue;
 
    for (int i = 0; i < length; i++) {
        int x = arr[i].first.first;
        int y = arr[i].first.second;
        int myRoom = 0;
 
        if (!priorityQueue.empty()) {
            int end, start, room;
            tie(end, start, room) = priorityQueue.top();
            priorityQueue.pop();
 
            if (end < x) {
                priorityQueue.push(make_tuple(y, x, room));
                myRoom = room;
            } else {
                priorityQueue.push(make_tuple(y, x, roomNext));
                myRoom = roomNext;
                priorityQueue.push(make_tuple(end, start, room));
                roomNext++;
            }
        } else {
            priorityQueue.push(make_tuple(y, x, roomNext));
            myRoom = roomNext;
            roomNext++;
        }
 
        count = max(static_cast<int>(priorityQueue.size()), count);
        rooms[arr[i].second] = myRoom;
    }
 
    cout << count << endl;
 
    for (int i = 0; i < length; i++) {
        cout << rooms[i] << " ";
    }
 
    cout << endl;
 
    return 0;
}