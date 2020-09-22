#include <iostream>
#include <stdio.h>
#include <time.h>
#include <algorithm>
#include <cstring>


using namespace std;

const int T=1000000000;

int main()
{

    float a=3.1415926535898,b=30.1415926535898,c=300.14159265358,d;

    for(int i=0;i<T;i++){
            d=a*b*b*a+c*a*b*c;
    }
    printf("%.2f\n",(double)T/((double)clock()/CLOCKS_PER_SEC));

    return 0;
}