#include <stdio.h>
int main(int argc, char *argv[]) {
    int array[100000],size=sizeof(array)/sizeof(array[0]),c,i,j,temp;
    for (c=0;c<10000000;c++) {
        for (i=0;i<size;i++) array[i] = i;
        for (i=0;i<size;i++) {
            for (j=0;j<size-1-i;j++) {
                if (array[j] < array[j+1]) {
                    temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
    for (i=0;i<size;i++) printf("%d ", array[i]);
    printf("\n");
    return 0;
}