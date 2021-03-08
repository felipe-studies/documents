#include <stdio.h>
#include <stdlib.h>

int main() {
	int a[4];
	a[0] = 1;
       	a[1] = 2;
	a[2] = 3;
	for (int i = 0; i < 3; i++) {
		printf("%d\n", a[i]);
	}	
	return 0;
}
