// Insertion Sort: https://www.youtube.com/watch?v=i-SKeOcBwko
//Selection sort: https://www.youtube.com/watch?v=GUDLRan2DWM
#include <bits/stdc++.h>

using namespace std;

void selection_sort(vector<int> arr ){
    return;
}

void insertion_sort(vector<int> arr) {
    int n = arr.size();
    for (int i = 1;i< n;i++) {
        int key = arr[i];
        int j = i - 1;
        while (j > -1 && arr[j] > key) {
            arr[j] = key;
            j = j - 1; 
        }
        arr[j+1] = arr[j];
    }

    return;
}

int main() {
    vector<int> arr(10);
    arr = [12,11,3,6,2,9,16,0,10,13];
}