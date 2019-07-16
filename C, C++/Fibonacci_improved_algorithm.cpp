// improved Fibonacci algorithm(fib2)
//////////////////////////////////////////////////////////////////////////
// compared to fib() function, fib2 is just called only one time for one required value.
// If the calculation time of the each calls would be 10^(-8) sec, 
// to get the 43th Fibonacci value, it takes about 14 secs,
// while for the fib2 algorithm gives the result in an instant.

// i: 0 cnt :1 1
// i: 1 cnt :1 1
// i: 2 cnt :3 2
// i: 3 cnt :5 3
// i: 4 cnt :9 5
// i: 5 cnt :15 8
// i: 6 cnt :25 13
// i: 7 cnt :41 21
// i: 8 cnt :67 34
// i: 9 cnt :109 55
// i: 10 cnt :177 89
// ...
// i: 40 cnt :331160281 165580141
// i: 41 cnt :535828591 267914296
// i: 42 cnt :866988873 433494437
// i: 43 cnt :1402817465 701408733

// i: 0 cnt2 :1 1
// i: 1 cnt2 :1 1
// i: 2 cnt2 :1 2
// i: 3 cnt2 :1 3
// i: 4 cnt2 :1 5
// i: 5 cnt2 :1 8
// i: 6 cnt2 :1 13
// i: 7 cnt2 :1 21
// i: 8 cnt2 :1 34
// i: 9 cnt2 :1 55
// i: 10 cnt2 :1 89
// ...
// i: 40 cnt2 :1 165580141
// i: 41 cnt2 :1 267914296
// i: 42 cnt2 :1 433494437
// i: 43 cnt2 :1 701408733
//////////////////////////////////////////////////////////////////////////
#include <iostream>

int cnt = 0;
int fib(int n){
  cnt ++;
  if(n<=1){
    return 1;
  }
  else{
    return fib(n-2) + fib(n-1);
  }
}

int cnt2 = 0;
int fib2(int n, int* pList){
  cnt2 ++;
  if(n<=1){
    return pList[n];
  }
  else{
    pList[n] = pList[n-2] + pList[n-1];
    return pList[n];
  }
}

int main() {
  std::cout << "How many fib series to print?\n";
  int n;

  std::cin >> n;
  for(int i=0; i<=n; i++){
    int temp = fib(i);
    std::cout << "i: " << i << " cnt :" << cnt << " " << temp << "\n";
    cnt = 0;
  }
  
  int fib2_list[n];
  fib2_list[0] = 1;
  fib2_list[1] = 1;
  for(int i=0; i<=n; i++){
    int temp = fib2(i, fib2_list);
    std::cout << "i: " << i << " cnt2 :" << cnt2 << " " << temp << "\n";
    cnt2 = 0;
  }
}
