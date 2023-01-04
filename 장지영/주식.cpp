#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

vector<string> split(string str, char delimiter);

int jonbuh_end(char **curr_list, int N) {
    
    int idx = max(curr_list);

    return 0;
}


int main() {
    int t;
    int n;
    cin >> t;
    
    for(int i = 0; i < t; i++) {
        cin >> n;
        char up_down[1000000];
        vector<string> result = split(up_down, ' ');
        for (int i = 0; i < result.size(); i++) {
            cout << result[i] << endl;
        }
    }

    return 0;
}
