#include <iostream>
#include <typeinfo>

// 사람이 기다릴 수 있을 만한 시간 안에 임무를 마치지 못하는 좋지 않은 알고리즘을 살펴본다.
// 피보나치 수열은 정의대로 재귀함수를 사용하면 간단히 구현할 수 있지만, 매우 느리다.
// fib(5)를 구하는데 fib(3)과 fib(4)를 호출하고, fib(3)은 다시 fib(1), fib(2)를 호출하고...
// fib(4)에서도 fib(2), fib(3)을 호출 하는 식으로 중복해서 호출을 하게 된다.

// fib(0) [count(1)] : 1
// fib(1) [count(1)] : 1
// fib(2) [count(3)] : 2
// fib(3) [count(5)] : 3
// fib(4) [count(9)] : 5
// fib(5) [count(15)] : 8
// fib(6) [count(25)] : 13
// fib(7) [count(41)] : 21
// fib(8) [count(67)] : 34
// fib(9) [count(109)] : 55

int count = 0;
 int fib(int n){
  count += 1;
  if(n<=1){
    return 1;
  }
  else{
    return fib(n-2) + fib(n-1);
  }
}

int fac(int n){
  if(n<=1){
    return 1;
  }
  else{
    return n*fac(n-1);
  }
}

int main() {
  for(int i=0; i<10; i++){
    int temp = fib(i);
    std::cout << "fib(" << i << ") [count(" << count << ")] : " << temp << "\n";
    count = 0;
  }

  for(int i=0; i<10; i++){
    std::cout << "fac(" << i << ") : " << fac(i) << "\n";
  }
}
