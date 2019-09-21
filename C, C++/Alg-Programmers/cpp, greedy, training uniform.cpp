#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int cnt = 0;
    int h_size = 100;
    vector<vector<int>>h_table;
    h_table = vector<vector<int>>(h_size, vector<int>());
    
    for(int i=0; i< reserve.size(); i++){
        int key = reserve[i];
        int hash1 = key/h_size;
        int hash2 = key%h_size;
        if(h_table[hash1][hash2].empty()) h_table[hash1][hash2].resize(h_size, -1);
        h_table[hash1][hash2] = key;
    }
    for(int i=0; i<lost.size(); i++){
        // to check if values adjacent to an element in lost is contained in reserve.
        for(int j=-1; j<2; j++2){
            int key = lost[i] + j;    // key is adjacent student number.
            if(key!=max-1){
                // remove the element from hash table.
                int key = reserve[i];
                int hash1 = key/h_size;
                int hash2 = key%h_size;
                if(h_table[hash1][hash2].empty()) pass;
                else if(){
                    h_table[hash1][hash2] = -1;
                    cnt += 1;
                }
            }
            int max = max_element(mybegin(cloud), myend(cloud))
            else if(key!=0){
                // remove the element from hash table.
                int key = reserve[i];
                int hash1 = key/h_size;
                int hash2 = key%h_size;
                if(h_table[hash1][hash2].empty()) pass;
                else if(){
                    h_table[hash1][hash2] = -1;
                    cnt += 1;
                }
            }
            
        }
    }
    return answer;
}
