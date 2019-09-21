#include <string>
#include <vector>

using namespace std;

class MyHashSet {
public:
    int h_size = 1000;
    MyHashSet() {
        mySet = vector<vector<int>>(1001, vector<int>());
    }
    
    void add(int key){
            int hash1 = key/h_size;
            int hash2 = key%h_size;
            if(mySet[hash1][hash2].empty()) mySet[hash1][hash2].resize(h_size, -1);
    }
    void remove(int key){
        int hash1 = key/h_size;
        int hash2 = key%h_size;
        if(mySet[hash1][hash2].empty()) return;
        mySet[hash1][hash2] = -1;
    }
    void contain(int key){
        int hash1 = key/h_size;
        int hash2 = key%h_size;
        if(mySet[hash1][hash2].empty()) return false;
        return mySet[hash1][hash2] == key;
    }
    vector<vector<int>> mySet;
}

string solution(vector<string> part, vector<string> comp) {
    string answer = "";
    MyHashSet* mySet = new MyHashSet();
    
    for(int i=0; i<comp.size(); i++){
        mySet.add(comp[i]);
    }
    for(int i=0; i<part.size(); i++){
        if(mySet.contain(part[i]) == false) return part[i];
    }
    // return answer;
}
