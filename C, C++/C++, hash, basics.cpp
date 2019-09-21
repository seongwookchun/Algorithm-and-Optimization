// This source code is based on the leetcode user woziji

class MyHashSet {
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        mySet = vector<vector<int>>(1001, vector<int>());
    }
    
    void add(int key) {
        int hash1 = key/1000;
        int hash2 = key%1000;
        if(mySet[hash1].empty()) mySet[hash1].resize(1000, -1);
        // vector.resize(n, val)
        // resize method is simle way to pad the value with val into n-th element
        // if n is lower than the original size of the vector,
        // then the method just gives elements from beginning to the n-th element,
        // and the rest of the elements after the n-th element are thrown away.
        mySet[hash1][hash2] = key;
    }
    
    void remove(int key) {
        int hash1 = key/1000;
        int hash2 = key%1000;
        if(mySet[hash1].empty()) return;   // The command return is an efficient way
                                           // to flee away from the function block.
        mySet[hash1][hash2] = -1;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int hash1 = key/1000;
        int hash2 = key%1000;
        if(mySet[hash1].empty()) return false;
        return mySet[hash1][hash2] == key;    // A nice way to give true value
                                              // with the conditional statement
        
    }
    vector<vector<int>> mySet;    // This line is needed.
                                  // if not, 
                                  // soultion.cpp: In constructor 'MyHashSet::MyHashSet()':
                                  // Line 5: Char 9: error: 'mySet' was not declared in this scope
                                  //          mySet = vector<vector<int>>(1001, vector<int>());
                                  //          ^~~~~
};
