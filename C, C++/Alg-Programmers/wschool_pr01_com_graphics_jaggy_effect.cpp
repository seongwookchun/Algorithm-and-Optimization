#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;


int solution(float n, float m) {
    float q = n/m;
    // cout << q;
    float tot = 0;
    int cnt = 0;
    // int i = 0;
    // cout << "hi in solution" << endl;
    for (int i=0; i<m; i++) {

        int ceil01 = floor(tot);
        int ceil02;
        tot += q;
        ceil02 = floor(tot);
        // https://www.quora.com/How-do-I-check-if-a-number-is-integer-on-C++
        if (ceil01 != ceil02) {
            if (ceil(tot) != floor(tot)) {
                cnt += 2;
            }
            else {
                cnt += 1;
            }
        }
        else {
            cnt += 1;
        }
        // cout << "solution(" << n << "," << m << ") : " << i << " " << ceil01 << " " << ceil02 << " " << left << setw(10) << tot << " " << cnt << endl;
    }
    return cnt;
}
int solution02(int n, int m) {
    return m + n -1;
}
int main() {
    cout << solution(2,3) << endl;
    cout << solution(2,5) << endl;
    cout << solution02(2,3) << endl;
    cout << solution02(2,5) << endl;
}
