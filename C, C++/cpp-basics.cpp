#include <iostream>

using namespace std; 
  
int main() 
{ 
    for(int i=0; i<10; i++){
        cout << i << '\n';
        if (i==5){
            cout << "hi \n";
            break;    // the command break makes flee away from the code block surrounding the command line.
        } 

    }
} 
