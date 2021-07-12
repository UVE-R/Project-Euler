//Optimal solution

#include <bits/stdc++.h>
using namespace std;

int p[10000] = {3,5,7}, i, j;
int k, n, flag;

int main() {

  for(i = 9, n = 2;; i += 2){
    j = sqrt(i);

    //check if i is prime, if it is NOT then j=0
    for(k = 0; p[k] <= j; k++){
            if(i % p[k] == 0){
               j = 0;
            }
    }

    if(j){
        p[++n] = i; //if a divisor is not found, n is a new prime and add it to the array
    }else{
        for(k = flag = 0; p[k] < i && p[k]; k++){

        j = sqrt((i - p[k]) / 2); //calculate  the base of the square

        if(j * j * 2 + p[k] == i){ //check if the base of the square is an integer
            flag = 1; //number found
            break;
        }
      }
      if(!flag){ //stops when the number is found
            break;
      }
    }
  }

  cout<<i<<endl;
  return 0;
}
