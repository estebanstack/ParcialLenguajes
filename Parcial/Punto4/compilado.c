#include <stdio.h>
#include <time.h>

int factorial(int n) {
    if (n == 0 ){
     	return 1;
    }
    else{
    	return n*factorial(n-1);
    }
    
}

int main() {
    int n = 40; 
    clock_t start = clock();

    int result = factorial(n);

    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Factorial(%d) = %lld\n", n, result);
    printf("Tiempo en C: %f segundos\n", time_taken);

    return 0;
}
