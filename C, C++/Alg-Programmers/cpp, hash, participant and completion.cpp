#include <string>
#include <vector>

using namespace std;

string solution(vector<string> part, vector<string> comp) {
    string answer = "";
    
    vector<vector<int>> mySet();
    int h_size = 1000;
    void add(key){
        hash1 = key/h_size;
        hash2 = key%h_size;
        if(mySet[hash1][hash2].empty()) mySet[hash1][hash2].resize(h_size, -1);
    }
    void remove(key){
        hash1 = key/h_size;
        hash2 = key%h_size;
        if(mySet[hash1][hash2].empty()) return;
        mySet[hash1][hash2] = -1;
    }
    void contain(key){
        hash1 = key/h_size;
        hash2 = key%h_size;
        if(mySet[hash1][hash2].empty()) return false;
        return mySet[hash1][hash2] == key;
    }
    
    for(int i=0; i<comp.size(); i++){
        add(comp[i]);
    }
    for(int i=0; i<part.size(); i++){
        if(contain(part[i]) == false) return part[i]
    }
    // return answer;
}
