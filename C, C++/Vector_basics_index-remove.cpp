#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    // initializing with input value, n and size of lost vector.
    int nb_ok = n - lost.size();

    for (int i=0; i < lost.size(); i++) { 
        cout << lost[i] << endl;
        int l = lost[i] - 1;
        int r = lost[i] + 1;
        for (int j=0; j<reserve.size(); j++) {
            if (reserve[j] == l or reserve[j] == r) {
                nb_ok ++;
                reserve.erase(reserve.begin()+j);
                // cout << "erased reserve vec : " << reserve << endl;
                break;
            }
        }
    }
    int answer = nb_ok;
    cout << "final nb_ok :" << nb_ok << endl;
    return answer;
}
