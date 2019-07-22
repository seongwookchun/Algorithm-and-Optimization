// 4장 기본 알고리즘 - 수학


#include <stdio.h>
#include <math.h>


// sec 016 소수 판별
// 유형 1 나누어 떨어지지 않을 때

// int main(void){
//   // char a;
//   // char* pa;
//   int a;    // 이 두 줄을 하나로 합치자.
//   int i, j; // 이 두 줄을 하나로 합치자.
//   j = 2;
//   scanf("%d", &a);
//   printf("a:%d\n", a);
//   i = a-1;
//   while(j <= i){
//     if(a%j == 0){
//       printf("not a prime number.");
//     }
//     else{
//       j++;
//     }
//     printf("i:%d/ j:%d/ a:%d \n", i, j, a);
//   }
//   if(j==a){
//     printf("%d is a prime number", a);
//   }
  // 위 방식은 while loop 후 if 블록에서 확인하는데 다른 더 좋은 방법은 없을까?
  // while(1)
  //   if(j <= i){
  //     ...
  //   }
  //   else{
  //     printf("%d is a prime number", a);
  //     break;
  //   }
//   return 0;
// }


// sec 016 소수 판별
// 유형 2 나누어 떨어질 때

// int main(){
//   int a, i;
  
//   scanf("%d", &a);
//   printf("a:%d\n", a);
//   i = 2;
  
//     printf("i:%d\n", i);
//     if(i<a){
//       if(a%i == 0){
//         printf("not a prime number.");
//         if(a%i == 1){
//           printf("%d is a prime number", a);
//           // break;
//         }
//         printf("not a prime");
//         // break;
//         // break;
//       }
//       else{
//         i++;
//       }
//     }
//     else{
      
//     }
  
//   return 0;
// }

#include <stdlib.h>
#include <string.h>

char* isPrime(int n){
  int a, i;
  
  // scanf("%d", &a);
  a = n;
  printf("a:%d\n", a);
  i = 2;

  do{
    if(a%i == 0){
      if(i==a){
        printf("is a prime number!! \n");
        char *str = malloc(sizeof(char) * 20);
        strcpy(str, "prime");
        return str;
        // break;
      }
      printf("not a prime\n");
      char *str = malloc(sizeof(char) * 20);
      strcpy(str, "non-prime");
      return str;
      break;
    }
    else{
      i++;
      printf("i:%d/ rest:%d  \n", i, a%i);
      return "not possible return case";
    };
  } while(i <= a);
  
}

int main(){
  for(int i=2; i<= 9; i++){
    printf("i:%d / prime?:%s\n", i, isPrime(i));
  }
  return 0;
}
