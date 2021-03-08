#include <stdio.h>
#include <stdlib.h>

int main() {
    // Allocates storage
    char *hello_world = (char*)malloc(13 * sizeof(char));
    // Prints "Hello world!" on hello_world
    sprintf(hello_world, "%s %s!", "Hello", "world");
    printf(hello_world);

    return 0;
}